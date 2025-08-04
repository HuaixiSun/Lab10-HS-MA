# https://github.com/HuaixiSun/Lab10-HS-MA
# Partner 1 : Murat Atar
# Partner 2 : Huaixi Sun

import math
def square_root(a):
    try:
        if a < 0:
            raise ValueError("Cannot take square root of a negative number")
        return math.sqrt(a)
    except ValueError as e:
        raise e
def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except Exception as e:
        raise e


def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("division by zero")
    return b / a

def log(a, b):
    if a <= 0 or a == 1:
        raise ValueError("base must be greater than 0 and not equal to 1.")
    if b <= 0:
        raise ValueError("argument must be greater than 0.")
    return math.log(b, a)

def exp(a, b):
    return a ** b

