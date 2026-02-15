from flask import Flask
from .routes import api
from .swagger import init_swagger

def create_app():
    app = Flask(__name__)
    app.config["WTF_CSRF_ENABLED"] = False
    init_swagger(app)
    app.register_blueprint(api)
    return app
