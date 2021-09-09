from django.db import models
from django.contrib.gis.db import models as geo_models

import polyline
from django.contrib.gis.geos import LineString

class Activity(geo_models.Model):
    user = models.ForeignKey(
        'auth.user', 
        on_delete=models.CASCADE, 
        related_name='activities'
    )
    
    external_id = models.CharField(max_length=100)
    distance = models.FloatField(blank=True, null=True)
    moving_time = models.FloatField(default=0.0)
    elapsed_time = models.FloatField(default=0.0)
    name = models.CharField(max_length=200)
    activity_type = models.CharField(max_length=100)
    start_date = models.DateTimeField(blank=True, null=True)
    polylines = geo_models.LineStringField(blank=True, null=True)

    def __str__(self):
        return u"%s - %s" % (self.activity_type, self.name)

    class Meta:
        get_latest_by = 'start_date'
        ordering = ['-start_date']
        verbose_name = 'activity'
        verbose_name_plural = 'activities'

    def update_from_strava(self, act): 
        self.external_id = act.id
        self.distance = act.distance.num
        self.moving_time = act.moving_time.total_seconds()
        self.elapsed_time = act.elapsed_time.total_seconds()
        self.start_date = act.start_date
        self.name = act.name
        self.activity_type = act.type

        self.save()
        return self

    def update_encoded_polyline(self, encoded_polyline):
        decoded_polyline = polyline.decode(encoded_polyline, geojson=True)
        ls = LineString(decoded_polyline)
        self.polylines = ls

        self.save()
        return self
