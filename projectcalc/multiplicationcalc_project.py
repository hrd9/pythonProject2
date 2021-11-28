"""Multiplication Class for the project"""

from projectcalc.calculation_project import Calculation

class Multiplicationcalc(Calculation):
    """Defining the calculator class for multiplying two numbers"""

    def getoutput(self):
        """Performing the multiplication operation"""
        return self.value_a * self.value_b
