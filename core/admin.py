from django.contrib import admin
from core.models import Activity, User

class ActivityAdmin(admin.ModelAdmin):
    pass
    
class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(Activity, ActivityAdmin)
admin.site.register(User, UserAdmin)