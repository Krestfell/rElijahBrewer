import MyMath
import unittest
import sys

# Define a test class that inherits from unit test.TestCase


class TestMyMath(unittest.TestCase):

    # Test the add function from the MyMath library
    def testAddInt(self):
        # Test addition of two integers
        result = MyMath.add(1, 2)
        self.assertEqual(result, 3)

    def testAddFloats(self):
        # Test that adding a float and an integer returns the correct result
        result = MyMath.add(10.5, 2)
        self.assertEqual(result, 12.5)

    def testAddStrings(self):
        # Test that add will return concatenation
        result = MyMath.add('ABC', 'DEF')
        self.assertEqual(result, 'ABCDEF')

    def testMultiplyStrings(self):
        # Test multiplying a string by an integer
        result = MyMath.multiply('ABC', 2)
        self.assertEqual(result, 'ABCABC')

    def testDivide(self):
        # Test integer division
        result = MyMath.divide(5, 5)
        self.assertEqual(result, 1)

    def testAddNotEqual(self):
        # Test that adding two integers does not equal 3
        result = MyMath.add(1, 1)
        self.assertNotEqual(result, 3)

    def testGreaterThan(self):
        # Test that one integer is greater than another
        result = MyMath.greaterThan(2, 1)
        self.assertTrue(result)
        result = MyMath.greaterThan(2, 11)
        self.assertFalse(result)

    def testConvertFromC(self):
        # Test converting Celsius to Fahrenheit
        self.assertEqual(MyMath.convertFromC(-40), -40)
        self.assertEqual(MyMath.convertFromC(100), 212)
        self.assertEqual(MyMath.convertFromC(0), 32)


# Check if this module is being run as the main program
if __name__ == '__main__':
    # Add the '-v' flag to print more verbose output
    sys.argv.append('-v')
    # Run the tests in the TestMyMath class
    unittest.main()
