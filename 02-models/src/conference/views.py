"""
views.py

URL route handlers

Note that any handler params must match the URL route params.
For example the *say_hello* handler, handling the URL route '/hello/<username>',
  must be passed *username* as the argument.

"""
import logging
from google.appengine.api import users
from google.appengine.runtime.apiproxy_errors import CapabilityDisabledError

from flask import request, render_template, flash, url_for, redirect, g

from flask_cache import Cache

from conference import app
from decorators import login_required
from forms import ConferenceForm
from models import Conference


# Flask-Cache (configured to use App Engine Memcache API)
cache = Cache(app)

## Error handlers
# Handle 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# Handle 500 errors
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500


@app.before_request
def before_request():
    if request.path == url_for('warmup'):
        return
    user = users.get_current_user()
    if user:
        g.logged_text = 'Logout'
        g.logged_url = users.create_logout_url(url_for('home'))
    else:
        g.logged_text = 'Login'
        g.logged_url = users.create_login_url(url_for('home'))


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/conferences', methods=['GET', 'POST'])
@login_required
def list_conferences():
    """List all conferences"""
    conferences = Conference.query()

    return render_template(
        'list_conferences.html', conferences=conferences
    )

@app.route('/conferences/new', methods=['GET', 'POST'])
@login_required
def new_conference():
    form = ConferenceForm()
    if request.method == "POST" and form.validate_on_submit():
        conference = Conference(
            organizer=users.get_current_user().email()
        )
        form.populate_obj(conference)
        try:
            conference.put()
            conference_id = conference.key.id()
            flash(u'Conference %s successfully saved.' % conference_id, 'success')
            return redirect(url_for('list_conferences'))
        except CapabilityDisabledError:
            flash(u'App Engine Datastore is currently in read-only mode.', 'info')
            return redirect(url_for('list_conferences'))
    logging.info('Form errors: %s' % form.errors)
    return render_template('new_conference.html', form=form)


@app.route('/_ah/warmup')
def warmup():
    """App Engine warmup handler
    See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests

    """
    return ''

