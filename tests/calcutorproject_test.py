"""Class for testing the calculation operation for project 2"""
import pytest
from projectcalculator.maincalculator import Calculator

# Defining the Fixture
@pytest.fixture
def clear_history():
    """Calling the clear history Method"""
    Calculator.clear_history()

# pylint: disable=unused-argument, redefined-outer-name
def test_project_calculator_addition(clear_history):
    """Testing the addition operation"""
    assert Calculator.add_operation(2, 6) == 8

# pylint: disable=unused-argument, redefined-outer-name
def test_project_calculator_subtraction(clear_history):
    """Testing the subtraction operation"""
    assert Calculator.sub_operation(4, 2) == 2

# pylint: disable=unused-argument, redefined-outer-name
def test_project_calculator_multiplication(clear_history):
    """Testing the multiplication operation"""
    assert Calculator.multiply_operation(8, 2) == 16

# pylint: disable=unused-argument, redefined-outer-name
def test_project_calculator_divide(clear_history):
    """Testing the division operation"""
    assert Calculator.divide_operation(8, 4) == 2
