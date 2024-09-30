"""Simple Calculator module."""

def addition(a: int | float, b: int | float) -> int | float:
    '''
    Computes the sum of two numbers
    '''
    return a + b

def subtraction(a: int | float, b: int | float) -> int | float:
    '''
    Computes the subtraction of two numbers
    '''
    return a - b

def multiplication(a: int | float, b: int | float) -> int | float:
    '''
    Computes the product of two numbers
    '''
    return a * b

def division(a: int | float, b: int | float) -> int | float:
    '''
    Computes the product of two numbers
    '''
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a / b
