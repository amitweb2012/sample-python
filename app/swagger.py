from flasgger import Swagger

def init_swagger(app):
    app.config["SWAGGER"] = {
        "title": "Flask Calculator API",
        "uiversion": 3
    }
    Swagger(app)
