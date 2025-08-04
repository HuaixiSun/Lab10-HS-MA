# https://github.com/muratatar06/Lab10-HS-MA
# Partner 1: Murat Atar
# Partner 2: [Partner’s Name]
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

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("division by zero")
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid base or argument for logarithm")
    return math.log(b, a)


def exp(a, b):
    return a ** b


