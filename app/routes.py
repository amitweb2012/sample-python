from flask import Blueprint, request, jsonify
from .calculator import Calculator, is_even

api = Blueprint("api", __name__)
calc = Calculator()

@api.route("/add", methods=["POST"])
def add():
    data = request.json
    return jsonify(result=calc.add(data["a"], data["b"]))

@api.route("/subtract", methods=["POST"])
def subtract():
    data = request.json
    return jsonify(result=calc.subtract(data["a"], data["b"]))

@api.route("/multiply", methods=["POST"])
def multiply():
    data = request.json
    return jsonify(result=calc.multiply(data["a"], data["b"]))

@api.route("/divide", methods=["POST"])
def divide():
    data = request.json
    try:
        return jsonify(result=calc.divide(data["a"], data["b"]))
    except ValueError as e:
        return jsonify(error=str(e)), 400

@api.route("/is-even", methods=["GET"])
def check_even():
    number = int(request.args.get("number"))
    return jsonify(is_even=is_even(number))
