"""Calculation Class"""

class Calculation:
    """Calculation Constructor"""
    # pylint: disable=too-few-public-methods

    # Implementation of the Encapsulation Feature
    def __init__(self, value_a, value_b):
        """Encapsulation Method"""
        self.value_a = value_a
        self.value_b = value_b

    # Implementation of the Encapsulation Feature
    @classmethod
    def create(cls, value_a, value_b):
        """ Returning the values back """
        return cls(value_a, value_b)
