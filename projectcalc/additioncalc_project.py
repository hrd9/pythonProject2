"""Addition Class for the project"""

from projectcalc.calculation_project import Calculation

#Implementation of the Inheritance Feature
class Additioncalc(Calculation):
    """Defining the calculator class for adding two numbers"""

    def getoutput(self):
        """Performing the addition operation"""
        return self.value_a + self.value_b
