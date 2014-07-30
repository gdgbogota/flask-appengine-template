"""
forms.py

Web forms based on Flask-WTForms

See: http://flask.pocoo.org/docs/patterns/wtforms/
     http://wtforms.simplecodes.com/

"""

from flaskext import wtf
from wtforms.ext.appengine.ndb import model_form

from .models import Conference

from wtforms.widgets.core import Input

ConferenceForm = model_form(Conference, wtf.Form,
                            exclude=['organizer', 'num_tix_available'],
                            field_args={
                                'name': dict(
                                    label='Conference Title'
                                ),
                                'desc': dict(
                                    label='Description'
                                ),
                                'start_date': dict(
                                    widget=Input(input_type='date')
                                ),
                                'end_date': dict(
                                    widget=Input(input_type='date')
                                ),
                            })
