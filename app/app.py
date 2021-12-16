"""A simple flask web app"""
from flask import Flask
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from app.controllers.pylint_controller import PylintController
from app.controllers.evolution_controller import EvolutionController
from app.controllers.aaaarticle_controller import AAAcontroller
from app.controllers.inventors_controller import InventorsController

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()

@app.route("/basicform", methods=['GET'])
def calculator_get():
    return CalculatorController.get()

@app.route("/basicform", methods=['POST'])
def calculator_post():
    return CalculatorController.post()

@app.route("/evolution", methods=['GET'])
def evolution_get():
    return EvolutionController.get()

@app.route("/inventors", methods=['GET'])
def inventors_get():
    return InventorsController.get()

@app.route("/aaatesting", methods=['GET'])
def aaatesting_get():
    return AAAcontroller.get()

@app.route("/pylint", methods=['GET'])
def pylint_get():
    return PylintController.get()
