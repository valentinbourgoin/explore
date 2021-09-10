from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.gis.db import models as geo_models
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.geos import Polygon, Point
import math

from explore import settings
from core.models import User

'''
Grid
'''
class Grid(geo_models.Model):
    SATUS_OPENED = "OPENED"
    STATUS_CLOSED = "CLOSED"
    STATUS_CHOICES = [
        (SATUS_OPENED, _("Opened")),
        (STATUS_CLOSED, _("Closed")),
    ]

    registered_users = models.ManyToManyField(
        User,
        related_name="registered_grids"
    )
    name = models.CharField(max_length=255)
    number_of_tiles_per_side = models.PositiveIntegerField(
        default=settings.MIN_NUMBER_OF_TILES_PER_SIDE,
        validators=[
            MinValueValidator(settings.MIN_NUMBER_OF_TILES_PER_SIDE), 
            MaxValueValidator(settings.MAX_NUMBER_OF_TILES_PER_SIDE)
        ]
    )
    center_point = geo_models.PointField()
    tile_size = models.FloatField(
        default=settings.DEFAULT_TILE_PERIMETER
    )
    status = models.CharField(
        max_length=12,
        choices=STATUS_CHOICES,
        default=SATUS_OPENED,
    )
    created_at = models.DateTimeField(auto_now=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return u"%s (%d tiles)" % (self.name, self.number_of_tiles_per_side)

    def get_total_number_of_tiles(self):
        return self.number_of_tiles_per_side**2

    def save(self, *args, **kwargs):
        super(Grid, self).save(*args, **kwargs)

        # @todo : Si le point central change ? 
        if (not self.tiles.exists()):
            print(u"Zones creation around %s" % self.center_point)
            for i in range(self.get_total_number_of_tiles()):
                print(u"Creating zone %d" % i)
                tile = Tile()
                tile.grid = self
                tile.grid_position = i
                # @todo : use signals + mixin 
                perimeter = self.tile_size
                nb = self.number_of_tiles_per_side
                xmin = self.center_point.x - ((nb / 2) * perimeter) + (math.floor(i / nb) * perimeter)
                ymin = self.center_point.y - ((nb / 2) * perimeter) + (i % nb * perimeter)  
                bbox = (xmin, ymin, xmin + perimeter, ymin + perimeter)
                tile.points = Polygon.from_bbox(bbox)

                print(tile.points)
                tile.save()


'''
Tile 
'''
class Tile(geo_models.Model):
    STATUS_UNLOCKED = 0
    STATUS_LOCKED = 1
    STATUS_CHOICES = [
        (STATUS_LOCKED, _('Locked')),
        (STATUS_UNLOCKED, _('Unlocked'))
    ]
    grid = models.ForeignKey(
        Grid, 
        on_delete=models.CASCADE,
        related_name="tiles"
    )
    points = geo_models.PolygonField()
    grid_position = models.PositiveIntegerField()
    status = models.IntegerField(
        choices=STATUS_CHOICES, 
        default=STATUS_UNLOCKED
    )
    activity_related = models.ForeignKey(
        "core.activity", 
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return u"Tile %s n°%d - (%s)" % (self.grid, self.grid_position, self.status)

    def lock(self, activity): 
        self.status = self.STATUS_LOCKED
        self.activity_related = activity
        self.save()
