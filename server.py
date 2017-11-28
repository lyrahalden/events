from flask import Flask, render_template, request

from jinja2 import StrictUndefined

from flask_debugtoolbar import DebugToolbarExtension

import os

from eventbrite import Eventbrite

import urllib

#get oauth token from env
EVENTBRITE_OAUTH_TOKEN = os.environ['EVENTBRITE_OAUTH_TOKEN']

#instantiate a global eventbrite API client
eventbrite = Eventbrite(EVENTBRITE_OAUTH_TOKEN)


app = Flask(__name__)

app.debug = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"
#change to True if debugging
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True


app.jinja_env.undefined = StrictUndefined

@app.route("/")
def index():
    """Display homepage"""

    return render_template("homepage.html")


@app.route('/search', methods=['POST'])
def search():
    """Search for events near you"""

    address = request.form.get("address")
    encoded_address = urllib.quote_plus(address)

    events = eventbrite.get("/events/search/?sort_by=distance&location.address=" + encoded_address)
    event_list = events['events']

    return render_template("results.html", events=event_list)

if __name__ == "__main__":

    app.jinja_env.auto_reload = app.debug  # make sure templates, etc. are not cached in debug mode

    # connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')
