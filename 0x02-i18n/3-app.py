#!/usr/bin/env python3
"""this docs contains Flask app"""

from flask import Flask, render_template, request
from flask_babel import Babel
from os import getenv


class Config(object):
    """
    class to Configuration for Babel
    is
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"

    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    func to Select and
    return best language match based
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def func_index() -> str:
    """
    func to
    Handles / route
    """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
