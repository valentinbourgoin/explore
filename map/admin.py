from django.contrib import admin
from map.models import Map, Zone

class MapAdmin(admin.ModelAdmin):
    pass

class ZoneAdmin(admin.ModelAdmin):
    pass

admin.site.register(Map, MapAdmin)
admin.site.register(Zone, ZoneAdmin)