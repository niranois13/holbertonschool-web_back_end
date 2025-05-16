#!/usr/bin/env python3
"6-app.py"
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz
from pytz.exceptions import UnknownTimeZoneError


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel()


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_locale():
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


def get_timezone():
    tz_param = request.args.get('timezone')
    if tz_param:
        try:
            return pytz.timezone(tz_param).zone
        except UnknownTimeZoneError:
            pass

    if g.get('user'):
        user_tz = g.user.get('timezone')
        if user_tz:
            try:
                return pytz.timezone(user_tz).zone
            except UnknownTimeZoneError:
                pass
    return 'UTC'


babel.init_app(app, locale_selector=get_locale, timezone_selector=get_timezone)


@app.before_request
def before_request():
    g.user = get_user()


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
