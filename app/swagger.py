from flasgger import Swagger

def init_swagger(app):
  swagger_config = {
      "headers": [],
      "specs": [
          {
              "endpoint": "apispec",
              "route": "/docs.json",
              "rule_filter": lambda rule: True,
              "model_filter": lambda tag: True,
          }
      ],
      "swagger_ui": True,
      "specs_route": "/docs/"
  }

  swagger_template = {
      "swagger": "2.0",
      "info": {
          "title": "Flask Calculator API",
          "version": "1.0.0"
      }
  }

  Swagger(app, config=swagger_config, template=swagger_template)
