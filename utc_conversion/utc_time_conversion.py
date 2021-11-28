import flask
from datetime import datetime
import pytz

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def utc_time():
    """
        Converts the UTC of the given timezone if the request contains a valid query string.
        If no query string is supplied, the local UTC timezone is used.

        Example of a request containing no query string: http://127.0.0.1:5000/
        Example of a valid query string: http://127.0.0.1:5000/?tz=Europe/Paris&hr=10&min=5`

        return: UTC time
        :rtype: str
     """
    if "tz" in flask.request.args:
        return datetime.now(pytz.timezone(flask.request.args.get("tz"))).utcnow().strftime('%H:%M UTC')
    else:
        return datetime.utcnow().time().strftime('%H:%M UTC')


app.run()
