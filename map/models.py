from django.db import models
from django.contrib.gis.db import models as geo_models
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.geos import Polygon, Point
import math

from explore import settings

'''
Map
'''
class Map(geo_models.Model):
    STATUS_IN_PROGRESS = "IN_PROGRESS"
    STATUS_FINISHED = "FINISHED"
    STATUS_CHOICES = [
        (STATUS_IN_PROGRESS, _("In progress")),
        (STATUS_FINISHED, _("Finished")),
    ]

    user = models.ForeignKey(
        "auth.user", 
        on_delete=models.CASCADE, 
        related_name="maps"
    )
    level = models.IntegerField(default=1)
    center_point = geo_models.PointField()
    status = models.CharField(
        max_length=12,
        choices=STATUS_CHOICES,
        default=STATUS_IN_PROGRESS,
    )
    created_at = models.DateTimeField(auto_now=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return u"Map Level %d - %s" % (self.level, self.user)

    def get_number_of_zones_per_slide(self):
        return (settings.MIN_NUMBER_OF_ZONES_PER_SIDE * self.level)

    def get_total_number_of_zones(self):
        return self.get_number_of_zones_per_slide()**2

    def save(self, *args, **kwargs):
        # @todo : Si le point central change ? 
        if (not self.zones.exists()):
            print(u"Zones creation around %s" % self.center_point)
            for i in range(self.get_total_number_of_zones()):
                print(u"Creating zone %d" % i)
                zone = Zone()
                zone.map = self
                zone.map_position = i
                # @todo : use signals + mixin 
                nb = self.get_number_of_zones_per_slide()
                perimeter = settings.ZONE_PERIMETER
                xmin = self.center_point.x - ((nb / 2) * perimeter) + (math.floor(i / nb) * perimeter)
                ymin = self.center_point.y - ((nb / 2) * perimeter) + (i % nb * perimeter)  
                bbox = (xmin, ymin, xmin + perimeter, ymin + perimeter)
                zone.points = Polygon.from_bbox(bbox)

                print(zone.points)
                zone.save()
        super(Map, self).save(*args, **kwargs)


'''
Zone 
'''
class Zone(geo_models.Model):
    STATUS_LOCKED = 0
    STATUS_UNLOCKED = 1
    STATUS_CHOICES = [
        (STATUS_LOCKED, _('Locked')),
        (STATUS_UNLOCKED, _('Unlocked'))
    ]
    map = models.ForeignKey(
        Map, 
        on_delete=models.CASCADE,
        related_name="zones"
    )
    points = geo_models.PolygonField()
    map_position = models.IntegerField()
    status = models.IntegerField(
        choices=STATUS_CHOICES, 
        default=STATUS_LOCKED
    )
    activity_related = models.ForeignKey(
        "core.activity", 
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return u"Zone %d - %s" % (self.map_position, self.map)
