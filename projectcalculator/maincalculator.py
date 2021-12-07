"""Main Calculator Operation Class"""
from projectcalc.additioncalc_project import Additioncalc
from projectcalc.subtractioncalc_project import Subtractioncalc
from projectcalc.multiplicationcalc_project import Multiplicationcalc
from projectcalc.divisioncalc_project import Divisioncalc
from projectcalc.history_project import History
from file_handler.read_csv import CSVFileRead


class Calculator:
    """Calling the calculator methods for performing operation"""

    temp = []
    data = []
    path = ''

    def __init__(self, path):
        self.data = CSVFileRead.read_userdata(path)
        self.path = path

    def get_userdata(self):
        """Taking the user data"""
        csv_userdata = self.data
        a = csv_userdata['a'].values
        b = csv_userdata['b'].values
        add_result = [round(i,3) for i in csv_userdata['add_result'].values]
        sub_result = [round(i,3) for i in csv_userdata['sub_result'].values]
        multiply_result = [round(i,3) for i in csv_userdata['multiply_result'].values]
        divide_result = [round(i,3) for i in csv_userdata['div_result'].values]

        return a, b, add_result, sub_result, multiply_result, divide_result

    @staticmethod
    def add_operation(*args):
        """Performing addition operation"""
        add = Additioncalc(args).getoutput()
        History.add_calculation_history(add)
        return History.get_last_calculation()

    @staticmethod
    def sub_operation(*args):
        """Performing subtraction operation"""
        sub = Subtractioncalc(args).getoutput()
        History.add_calculation_history(sub)
        return History.get_last_calculation()

    @staticmethod
    def multiply_operation(*args):
        """Performing multiply operation"""
        mul = Multiplicationcalc(args).getoutput()
        History.add_calculation_history(mul)
        return History.get_last_calculation()

    @staticmethod
    def divide_operation(*args):
        """Performing divide operation"""
        div = Divisioncalc(args).getoutput()
        History.add_calculation_history(div)
        return History.get_last_calculation()
