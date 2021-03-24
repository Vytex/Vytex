from app import app, scheduler
from app.models import Venue
from app.controller.admin_controller import admin_controller

# schedules the server to create the next days linelist for all venues
@scheduler.task('cron', id='create_tomorrows_list', hour=0, minute=1, second=0, misfire_grace_time=900)
def create_tomorrows_list():
    with app.app_context():
        venues = Venue.get_all()

        for venue in venues:
            admin_controller.create_list(venue.venue_id, venue.line_capacity, is_tomorrow=True)
