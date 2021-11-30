"""Triangle Class"""
from projectcalc.gemetriccalc_project import Geometric

class TriangleCalc(Geometric):
    """Defining the triangle class"""

    # pylint: disable=too-few-public-methods
    def __init__(self, name, base, height):
        """Defining the init function"""
        super().__init__(name)
        self.base = base
        self.height = height

    @classmethod
    def getresult(cls, base, height):
        """Returning the result"""
        return 0.5 * base * height
