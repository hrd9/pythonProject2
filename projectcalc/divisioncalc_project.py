"""Division Class for the project"""

from projectcalc.calculation_project import Calculation

class Divisioncalc(Calculation):
    """Defining the calculator class for dividing two numbers"""
    #Inheriting the methods from the parent class calculator
    def getoutput(self):
        """Performing the division operation"""
        return self.value_a / self.value_b
