"""Class for testing the calculation operation for project 2"""
import pytest
from projectcalculator.maincalculator import Calculator
from projectcalc.triangle_project import TriangleCalc
from projectcalc.circlecalc_project import CircleCalc

# Defining the Fixture
@pytest.fixture
def clear_history():
    """Calling the clear history Method"""
    Calculator.clear_history()

# pylint: disable=unused-argument, redefined-outer-name
def test_project_calculator_addition(clear_history):
    """Testing the addition operation"""
    assert Calculator.add_operation(2, 6) == 8
    assert Calculator.add_operation(10, 2) == 12
    assert Calculator.add_operation(2, 4) == 6

# pylint: disable=unused-argument, redefined-outer-name
def test_project_calculator_subtraction(clear_history):
    """Testing the subtraction operation"""
    assert Calculator.sub_operation(4, 2) == 2
    assert Calculator.sub_operation(5, 4) == 1
    assert Calculator.sub_operation(40, 30) == 10

# pylint: disable=unused-argument, redefined-outer-name
def test_project_calculator_multiplication(clear_history):
    """Testing the multiplication operation"""
    assert Calculator.multiply_operation(8, 2) == 16
    assert Calculator.multiply_operation(5, 2) == 10
    assert Calculator.multiply_operation(5, 5) == 25
    assert Calculator.multiply_operation(6, 8) == 48

# pylint: disable=unused-argument, redefined-outer-name
def test_project_calculator_divide(clear_history):
    """Testing the division operation"""
    assert Calculator.divide_operation(8, 4) == 2
    assert Calculator.divide_operation(50, 10) == 5

def test_project_triangle():
    """Testing triangle function"""
    assert TriangleCalc.getresult(10,20) == 100

def test_project_circle():
    """Testing the area of the circle"""
    assert CircleCalc.getresult(10) == 314
