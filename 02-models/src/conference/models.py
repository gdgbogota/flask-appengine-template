"""
models.py

App Engine datastore models

"""

from google.appengine.ext import ndb
import constants

class Conference(ndb.Model):
    organizer = ndb.StringProperty(required=True)
    name = ndb.StringProperty(required=True)
    desc = ndb.TextProperty()
    topic = ndb.StringProperty(choices=constants.TOPICS)
    city = ndb.StringProperty(choices=constants.CITIES)
    max_attendees = ndb.IntegerProperty()
    num_tix_available = ndb.IntegerProperty()
    start_date = ndb.DateProperty()
    end_date = ndb.DateProperty()
