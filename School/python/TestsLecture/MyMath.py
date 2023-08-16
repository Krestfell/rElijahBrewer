#MyMath.py

import math

def main():
      print(add(1, 2))
      print(subtract(10, 20))
      print(multiply(50, 240))
      print(divide(50, 10))

      


def add(a, b):
      return a + b

def subtract(a, b):
      return a - b

def multiply(a, b):
      return a * b

def divide(numerator, denominator):
      if denominator == 0:
            raise ZeroDivisionError
      elif type(denominator) == str:
            raise TypeError
      else:
            return numerator / denominator

      
def greater_than(a, b):
      return a > b
      '''if a > b:
            return True
      else:
            return False'''

def convertFromC(centigrade):
      return (centigrade * 9/5.0) + 32









if __name__ == '__main__':
      main()
