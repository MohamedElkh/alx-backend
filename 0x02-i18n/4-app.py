#!/usr/bin/env python3
"""Contains a basic flask app displaying 'Welcome to Holberton' on"""
from os import getenv
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__, static_url_path='')
babel = Babel(app)


class Config(object):
    """class to configuration for babel"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def func_index() -> str:
    """func to this route renders 0-index.html template"""
    return render_template('4-index.html')


@babel.localeselector
def get_locale() -> str:
    """func method checks the URL parameter for locale variable"""
    if request.args.get('locale'):
        req = request.args.get('locale')

        if req in app.config['LANGUAGES']:
            return req
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
