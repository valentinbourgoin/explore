from explore.celery import app

from core.models import Activity, User
from .models import Grid, Tile

@app.task 
def process_activity_tails(activity_id):
    print(u"Mapping activity %d" % activity_id)
    activity = Activity.objects.get(id=activity_id)
    grids = activity.user.registered_grids.filter(status="OPENED") # @todo custom queryset
    print(u"Number of grids to process: %d" % len(grids))
    for grid in grids:
        tiles = grid.tiles.filter(status=0) #@todo custom queryset
        print(u"Number of still available tiles for this grid: %d" % len(tiles))
        for tile in tiles:
            if tile.points.intersects(activity.polylines):
                print(u"New tile locked: %d. Nice job %s" % (tile.id, activity.user))
                tile.lock(activity)