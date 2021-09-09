from django.contrib import admin
from map.models import Grid, Tile

class GridAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "number_of_tiles_per_side", "tile_size")
    list_filter = ("status",)


class TileAdmin(admin.ModelAdmin):
    list_select_related=("grid", )
    list_display = ("grid_position", "grid_name", "status")
    list_filter = ("status", "grid__name")

    @admin.display(description='Grid name')
    def grid_name(self, obj):
        return u"%s" % obj.grid.name 

admin.site.register(Grid, GridAdmin)
admin.site.register(Tile, TileAdmin)