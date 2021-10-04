from flask import Flask


def get_app():
    web_app = Flask(__name__)
    from pages import bluePrint
    web_app.register_blueprint(bluePrint, url_prefix='/')

    return web_app
