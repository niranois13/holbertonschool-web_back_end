#!/usr/bin/env python3
"3-app.py"
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as flask_gettext


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel()

def _(message_id, **variables):
    """
    Mark a string for translation.

    Args:
        message_id (str): The message ID to translate.
        **variables: Optional named variables for string formatting.

    Returns:
        str: The translated string.
    """
    return flask_gettext(message_id, **variables)


def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index():
    """Renders index template"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)
