"""Main Calculator Operation Class"""
from projectcalc.additioncalc_project import Additioncalc
from projectcalc.subtractioncalc_project import Subtractioncalc
from projectcalc.multiplicationcalc_project import Multiplicationcalc
from projectcalc.divisioncalc_project import Divisioncalc

class Calculator:
    """Calling the calculator methods for performing operation"""

    temp_hist = []

    @staticmethod
    def get_last_operation_added():
        """ Gets last calculation from history array """
        return Calculator.temp_hist[-1]

    @staticmethod
    def add_operation_to_history(calculation):
        """ Appends calculation to history array """
        Calculator.temp_hist.append(calculation)

    @staticmethod
    def clear_history():
        """ Creating History method for clearing the calc history"""
        Calculator.temp_hist.clear()

    @staticmethod
    def add_operation(value_a, value_b):
        """Calling the addition method for performing operation"""
        addition = Additioncalc.create(value_a,value_b).getoutput()
        Calculator.add_operation_to_history(addition)
        return Calculator.get_last_operation_added()

    @staticmethod
    def sub_operation(value_a, value_b):
        """Calling the subtraction method for performing operation"""
        subtraction = Subtractioncalc.create(value_a, value_b).getoutput()
        Calculator.add_operation_to_history(subtraction)
        return Calculator.get_last_operation_added()

    # Implementing Factory Method
    @staticmethod
    def multiply_operation(value_a, value_b):
        """Calling the multiply method for performing operation"""
        multiply = Multiplicationcalc.create(value_a, value_b).getoutput()
        Calculator.add_operation_to_history(multiply)
        return Calculator.get_last_operation_added()

    #Implementing Factory Method
    @staticmethod
    def divide_operation(value_a, value_b):
        """Calling the division method for performing operation"""
        division = Divisioncalc.create(value_a, value_b).getoutput()
        Calculator.add_operation_to_history(division)
        return Calculator.get_last_operation_added()
