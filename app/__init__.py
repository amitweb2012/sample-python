from flask import Flask
from .routes import api
from .swagger import init_swagger

def create_app():
    app = Flask(__name__)
    app.config["WTF_CSRF_ENABLED"] = False
    app.register_blueprint(api)
    init_swagger(app)
    return app
