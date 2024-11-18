"""
Module for simple calculations
"""

class UnsupportedOperationError(Exception):
    """
    Custom error raised when an unsupported operation is encountered.
    """
    def __init__(self, message):
        super().__init__(message)

def calculate(op: str, arg1, arg2):
    """
    Perform simple calculations. Accepts 3 request parameters:
    :param op: name of the operation. Supported values: 'sum', 'sub', 'mul', 'div'
    :param arg1: first argument for operation
    :param arg2: second argument for operation
    :return: calculated result
    """
    match op:
        case "sum":
            return add(arg1, arg2)
        case "sub":
            return subtract(arg1, arg2)
        case "mul":
            return multiply(arg1, arg2)
        case "div":
            return divide(arg1, arg2)
        case _:
            raise UnsupportedOperationError('Invalid operation')


def add(a, b):
    """
    Adds two numbers
    :param a: argument 1
    :param b: argument 2
    :return: result of addition
    """
    return a + b


def subtract(a, b):
    """
    Subtracts two numbers
    :param a: argument 1
    :param b: argument 2
    :return: result of subtraction
    """
    return a - b


def divide(a, b):
    """
    Divides two numbers
    :param a: argument 1
    :param b: argument 2
    :return: result of division
    """
    return a / b


def multiply(a, b):
    """
    Multiplies two numbers
    :param a: argument 1
    :param b: argument 2
    :return: result of multiplication
    """
    return a * b
