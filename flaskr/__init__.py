import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from flaskr import t11

    @app.route('/ryan')
    def ryan():
        return t11.test1()

    return app