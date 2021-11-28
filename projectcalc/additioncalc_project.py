"""Addition Class for the project"""

from projectcalc.calculation_project import Calculation

class Additioncalc(Calculation):
    """Defining the calculator class for adding two numbers"""

    def getoutput(self):
        """Performing the addiiton operation"""
        return self.value_a + self.value_b
