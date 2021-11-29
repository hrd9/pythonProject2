"""Subraction Class for the project"""

from projectcalc.calculation_project import Calculation

#Implementation of the Inheritance Feature
class Subtractioncalc(Calculation):
    """Defining the calculator class for subtracting two numbers"""

    def getoutput(self):
        """Performing the subtracting operation"""
        return self.value_a - self.value_b
