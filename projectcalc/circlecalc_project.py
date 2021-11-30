"""Circle Class"""
from projectcalc.gemetriccalc_project import Geometric

class CircleCalc(Geometric):
    """Logic for calculating area of circle"""

    # pylint: disable=too-few-public-methods
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    @classmethod
    def getresult(cls, radius):
        """Returning the result"""
        result = 3.14 * radius ** 2
        return result
