from django.contrib import admin
from core.models import Activity, User, UserSync

class ActivityAdmin(admin.ModelAdmin):
    pass
    
class UserAdmin(admin.ModelAdmin):
    pass

class UserSyncAdmin(admin.ModelAdmin):
    pass

admin.site.register(Activity, ActivityAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(UserSync, UserSyncAdmin)