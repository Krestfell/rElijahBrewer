#test_MyMath.py

import MyMath
import unittest
import sys

class TestMyMath(unittest.TestCase):


      
      def test_add_integers(self):
            result = MyMath.add(1, 2)
            self.assertEqual(result, 3)

      def test_add_floats(self):
            result = MyMath.add(10.5, 2)
            self.assertEqual(result, 12.5)

      def test_subtract_integers(self):
            result = MyMath.subtract(5, 9)
            self.assertEqual(result, -4)

      def test_multiply_integers(self):
            result = MyMath.multiply(5, 4)
            self.assertEqual(result, 20)

      def test_divide_integers(self):
            result = MyMath.divide(150, 25)
            self.assertEqual(result, 6)

      def test_add_strings(self):
            result = MyMath.add('abc', 'qwert')
            self.assertEqual(result, 'abcqwert')

      def test_multiply_strings(self):
            result = MyMath.multiply('qwerty', 2)
            self.assertEqual(result, 'qwertyqwerty')

      def test_add_not_equal(self):
            result = MyMath.add(1, 1)
            self.assertNotEqual(result, 49)

      def test_greater_than(self):
            result = MyMath.greater_than(2, 1)
            self.assertTrue(result)
            result = MyMath.greater_than(2, 11)
            self.assertFalse(result)

      def test_convertFromC(self):
            self.assertEqual(MyMath.convertFromC(-40), -40)
            self.assertEqual(MyMath.convertFromC(100), 212)
            self.assertEqual(MyMath.convertFromC(0), 32)
            

if __name__ == '__main__':
      sys.argv.append('-v')
      unittest.main()
