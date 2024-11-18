"""
Provides API foo simple calculations
"""

from flask import Flask, request
from calculator import simple_calculator as calc


app = Flask(__name__)


@app.route('/calculate')
def calculate():
    """
    Endpoint that does simple calculations. Accepts 3 request parameters:
    op: name of the operation. Allowed values: 'sum', 'sub', 'mul', 'div'
    arg1: first argument for operation
    arg2: second argument for operation
    :return: calculated result
    """
    op = request.args.get('op', type=str)
    arg1 = request.args.get('arg1', type=int)
    arg2 = request.args.get('arg2', type=int)

    if arg1 is None or arg2 is None:
        return {'error': 'Argument is required'}, 400

    try:
        result = calc.calculate(op, arg1, arg2)
        return wrap_response(result)
    except (calc.UnsupportedOperationError, ZeroDivisionError) as e:
        return {'error': str(e)}, 400



if __name__ == '__main__':
    app.run()



def wrap_response(result, status_code=200):
    """
    Wraps result into response json with given status code
    :param result: result of calculation
    :param status_code: returned status code, defaults to 200
    :return: response json
    """
    return {"result": result}, status_code
