"""Division Class for the project"""

from projectcalc.calculation_project import Calculation

#Implementation of the Inheritance Feature
class Divisioncalc(Calculation):
    """Defining the calculator class for dividing two numbers"""

    def getoutput(self):
        """Performing the division operation"""
        return self.value_a / self.value_b
