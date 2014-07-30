"""
models.py

App Engine datastore models

"""

from google.appengine.ext import ndb


class Conference(ndb.Model):
    organizer = ndb.StringProperty(required=True)
    name = ndb.StringProperty(required=True)
    desc = ndb.StringProperty(indexed=False)
    topic = ndb.StringProperty()
    city = ndb.StringProperty()
    max_attendees = ndb.IntegerProperty()
    num_tix_available = ndb.IntegerProperty()
    start_date = ndb.DateProperty()
    end_date = ndb.DateProperty()
