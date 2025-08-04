# https://github.com/HuaixiSun/Lab10-HS-MA
# Partner 1: Murat Atar
# Partner 2: Huaixi Sun
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 5), 4)
        self.assertEqual(add(0, 0), 0)
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(0, 1), 1)
        self.assertEqual(calculator.add(-1, 2), 1)

    def test_subtract(self):
        self.assertEqual(calculator.sub(3, 2), 1)
        self.assertEqual(calculator.sub(1, 2), -1)
        self.assertEqual(calculator.sub(1, 0), 1)


    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-1, 5), -5)
        self.assertEqual(mul(0, 10), 0)

    def test_divide(self):  # 3 assertions
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(5, 25), 5)
        self.assertEqual(div(1, 7), 7)

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):  # 3 assertions
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 1000), 3)
        self.assertAlmostEqual(logarithm(4, 16), 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 1)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.log(2, 8), 3)
        self.assertAlmostEqual(calculator.log(-1, 1), 2)
        self.assertAlmostEqual(calculator.log(3, 9), 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.log(1, 10)

    ######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(2, -5)

    def test_hypotenuse(self):  # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(0, 7), 7)

    def test_sqrt(self):  # 3 assertions
        self.assertAlmostEqual(square_root(9), 3)
        self.assertAlmostEqual(square_root(16), 4)
        with self.assertRaises(ValueError):
            square_root(-1)

# Do not touch this
if __name__ == "__main__":
    unittest.main()