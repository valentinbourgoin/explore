from django.db import models
from django.contrib.gis.db import models as geo_models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.geos import LineString

import polyline
from allauth.socialaccount.models import SocialApp

'''
Explore user model
Extended Django auth model
'''
class User(AbstractUser):
    avatar = models.ImageField(upload_to="avatar")

'''
UserSync model
Link between User and social provider 
Used to store API response information / status 
'''
class UserSync(models.Model): 
    app = models.ForeignKey(
        SocialApp, 
        on_delete=models.CASCADE,
        related_name='user_syncs'
    )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='user_syncs'
    )
    last_updated_at = models.DateTimeField(auto_now_add=True)
    last_response = models.JSONField(blank=True, null=True)

    class Meta:
        unique_together = ("app", "user")
        verbose_name = _("User sync")

    def __str__(self):
        return u'%s (%s)' % (self.user, self.app)

'''
Sport activity model
Linked to a user and a provider 
Used to store both sport and GPS data
'''
class Activity(geo_models.Model):
    user = models.ForeignKey(
        User, 
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
