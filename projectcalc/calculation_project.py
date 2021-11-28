"""Calculation Class"""

class Calculation:
    """Calculation Constructor"""
    # pylint: disable=too-few-public-methods

    def __init__(self, value_a, value_b):
        """Self references"""
        self.value_a = value_a
        self.value_b = value_b

    @classmethod
    def create(cls, value_a, value_b):
        """ Returning the values back """
        return cls(value_a, value_b)
