"""Main Calculator Operation Class"""
from projectcalc.additioncalc_project import Additioncalc
from projectcalc.subtractioncalc_project import Subtractioncalc
from projectcalc.multiplicationcalc_project import Multiplicationcalc
from projectcalc.divisioncalc_project import Divisioncalc
from projectcalc.history_project import History

class Calculator:
    """Calling the calculator methods for performing operation"""

    @staticmethod
    def add_operation(tuple_values : tuple):
        """Performing addition operation"""
        History.add_calculation_history(Additioncalc.create(tuple_values).getoutput())
        return True

    @staticmethod
    def sub_operation(tuple_values : tuple):
        """Performing subtraction operation"""
        History.add_calculation_history(Subtractioncalc.create(tuple_values).getoutput())
        return True

    @staticmethod
    def multiply_operation(tuple_values : tuple):
        """Performing multiplication operation"""
        History.add_calculation_history(Multiplicationcalc.create(tuple_values).getoutput())
        return True

    @staticmethod
    def divide_operation(tuple_values : tuple):
        """Performing division operation"""
        History.add_calculation_history(Divisioncalc.create(tuple_values).getoutput())
        return True

    @staticmethod
    def get_last_value():
        """result of the calculation"""
        return History.get_last_calculation()
