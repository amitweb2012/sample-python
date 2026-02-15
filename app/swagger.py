from flasgger import Swagger

def init_swagger(app):
  swagger_config = {
      "headers": [],
      "specs": [
          {
              "endpoint": "apispec_1",
              "route": "/docs.json",   # JSON endpoint
              "rule_filter": lambda rule: True,
              "model_filter": lambda tag: True,
          }
      ],
      "static_url_path": "/flasgger_static",
      "swagger_ui": True,
      "specs_route": "/docs/"   # UI route
  }

  swagger_template = {
      "swagger": "2.0",
      "info": {
          "title": "Flask Calculator API",
          "description": "API for basic calculator operations",
          "version": "1.0.0"
      }
  }

  Swagger(app, config=swagger_config, template=swagger_template)
   