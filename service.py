import benfordapp

web_app = benfordapp.get_app()

def start_app():
    return web_app


if __name__ == '__main__':
    start_app()
    web_app.run(host='0.0.0.0', debug=False)
