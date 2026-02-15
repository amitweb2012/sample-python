from flasgger import Swagger

def init_swagger(app):
    app.config["SWAGGER"] = {
      "headers": [],
      "specs": [
          {
              "endpoint": 'apispec',
              "route": '/docs.json',
              "rule_filter": lambda rule: True,
              "model_filter": lambda tag: True,
          }
      ],
      "swagger_ui": True,
      "specs_route": "/docs/"
    }
    Swagger(app)
