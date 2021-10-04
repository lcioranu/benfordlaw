from flask import Flask


def getApp():
    webApp = Flask(__name__)
    from pages import bluePrint
    webApp.register_blueprint(bluePrint, url_prefix='/')

    return webApp
