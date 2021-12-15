from app.controllers.controller import ControllerBase
from projectcalculator.maincalculator import Calculator
from flask import render_template, request, flash, redirect, url_for
import pandas as pd

class CalculatorController(ControllerBase):
    @staticmethod
    def post():

        # get the values out of the form
        value1 = request.form['value1']
        value2 = request.form['value2']
        operation = request.form['operation']

        if request.form['value1'] == '' and request.form['value2'] == '':
            flash('Oops! Please enter the validate input for performing operations')
        elif request.form['value1'] == '':
            flash('The value of field 1 needs to be inserted')
        elif request.form['value2'] == '':
            flash('The value of field 2 needs to be inserted')
        elif request.form['value2'] == '0' and operation == 'division' :
            flash('Division by Zero Exception occurred !!')
        else:
            flash('Operation performed successfully !!!!')

            # make the tuple
            my_tuple = (value1, value2)
            # this will call the correct operation
            getattr(Calculator, operation)(my_tuple)
            result = str(Calculator.get_last_value())

            #CSV Write logic
            calc_obj = {'Value1': [value1], 'Value2': [value2], 'Operation': [operation], 'Result': [result]}
            df = pd.Dataframe(calc_obj, columns=['Value1', 'Value2', 'Operation', 'Result'])
            df.to_csv('projectoutput.csv', mode='a', index=False, header=False, sep=',')

            hist = pd.read_csv('projectoutput.csv', skiprows=1).values.tolist()

            return render_template('result.html', value1=value1, value2=value2, operation=operation, result=result, hist=hist)
        return render_template('basicform.html')

    @staticmethod
    def get():
        return render_template('basicform.html')