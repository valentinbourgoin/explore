from celery.utils.log import get_task_logger

from core.models import Activity
from core.backend.strava import StravaClient

from explore.celery import app

logger = get_task_logger(__name__)

@app.task()
def process_activity(activity_id):
    logger.info(u"Getting details for activity %d" % activity_id)
    activity = Activity.objects.get(id=activity_id)
    client = StravaClient(activity.user).client
    act = client.get_activity(activity.external_id)
    activity.update_encoded_polyline(act.map.polyline)

    logger.info(u"Mapping activity %d" % activity_id)
    # @todo custom queryset
    grids = activity.user.registered_grids.filter(
        status="OPENED", 
        date_begin__lte=activity.start_date,
        date_end__gte=activity.start_date
    ) 
    logger.info(u"Number of grids to process: %d" % len(grids))
    result = { 'new_locked_tiles': [] }
    for grid in grids:
        tiles = grid.tiles.filter(status=0) # @todo custom queryset
        logger.info(u"Number of still available tiles for this grid: %d" % len(tiles))
        for tile in tiles:
            if tile.points.intersects(activity.polylines):
                logger.info(u"New tile locked: %d. Nice job %s" % (tile.id, activity.user))
                tile.lock(activity)
                result['new_locked_tiles'].append(tile.id)
    return result