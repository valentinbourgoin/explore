from django.contrib import admin
from core.models import Activity

class ActivityAdmin(admin.ModelAdmin):
    pass
admin.site.register(Activity, ActivityAdmin)