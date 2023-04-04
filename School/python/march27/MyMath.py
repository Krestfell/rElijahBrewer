import math


def main():
    # Testing the functions
    print(add(1, 2))
    print(subtract(10, 20))
    print(multiply(50, 240))
    print(divide(50, 10))


def add(a, b):
    """Returns the sum of two numbers"""
    return a + b


def subtract(a, b):
    """Returns the difference between two numbers"""
    return a - b


def multiply(a, b):
    """Returns the product of two numbers"""
    return a * b


def divide(numerator, denominator):
    """Returns the result of dividing two numbers"""
    if denominator == 0:
        # If denominator is 0, raise a ZeroDivisionError
        raise ZeroDivisionError("Cannot divide by zero")
    elif not isinstance(denominator, (int, float)):
        # If denominator is not a number, raise a TypeError
        raise TypeError("Denominator must be a number")
    else:
        return numerator / denominator


def greater_than(a, b):
    """Returns True if a is greater than b, False otherwise"""
    return a > b


def convert_from_celsius(centigrade):
    """Converts temperature from Celsius to Fahrenheit"""
    return (centigrade * 9/5) + 32


if __name__ == "__main__":
    main()
