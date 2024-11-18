import unittest as ut
import simple_calculator as calc


class SimpleCalculatorTest(ut.TestCase):

    def test_should_raise_error_when_invalid_arguments(self):
        self.assertRaises(calc.UnsupportedOperationError, calc.calculate, "invalid", 1, 2)
        self.assertRaises(TypeError, calc.calculate, "sum", "invalid", 2)
        self.assertRaises(TypeError, calc.calculate, "sum", 1, "invalid")
        self.assertRaises(ZeroDivisionError, calc.calculate, "div", 1, 0)

    def test_add_numbers(self):
        self.assertEqual(calc.calculate("sum", 1, 2), 3, "Invalid result of add operation")
        self.assertEqual(calc.calculate("sum", 1, 0), 1, "Invalid result of add operation")
        self.assertEqual(calc.calculate("sum", 1, -3), -2, "Invalid result of add operation")
        self.assertEqual(calc.calculate("sum", -1, 4), 3, "Invalid result of add operation")
        self.assertEqual(calc.calculate("sum", 0, 0), 0, "Invalid result of add operation")
        self.assertEqual(calc.calculate("sum", 1.2, 2), 3.2, "Invalid result of add operation")
        self.assertEqual(calc.calculate("sum", 99999999999, 90000000000000000000000), 90000000000099999999999, "Invalid result of add operation")

    def test_subtract_numbers(self):
        self.assertEqual(calc.calculate("sub", 2, 1), 1, "Invalid result of subtraction")
        self.assertEqual(calc.calculate("sub", 2, 4), -2, "Invalid result of subtraction")
        self.assertEqual(calc.calculate("sub", -2, 4), -6, "Invalid result of subtraction")
        self.assertEqual(calc.calculate("sub", -2, -5), 3, "Invalid result of subtraction")
        self.assertEqual(calc.calculate("sub", 8.5, 5), 3.5, "Invalid result of subtraction")
        self.assertEqual(calc.calculate("sub", 8, 5.5), 2.5, "Invalid result of subtraction")

    def test_multiply_numbers(self):
        self.assertEqual(calc.calculate("mul", 2, 3), 6, "Invalid result of multiplication")
        self.assertEqual(calc.calculate("mul", -2, 3), -6, "Invalid result of multiplication")
        self.assertEqual(calc.calculate("mul", 2, -3), -6, "Invalid result of multiplication")
        self.assertEqual(calc.calculate("mul", 2, 0), 0, "Invalid result of multiplication")
        self.assertEqual(calc.calculate("mul", 0, 0), 0, "Invalid result of multiplication")
        self.assertEqual(calc.calculate("mul", 0, 5), 0, "Invalid result of multiplication")
        self.assertEqual(calc.calculate("mul", 4, 0.5), 2, "Invalid result of multiplication")

    def test_divide_numbers(self):
        self.assertEqual(calc.calculate("div", 4, 2), 2, "Invalid result of division")
        self.assertEqual(calc.calculate("div", 1, 2), 0.5, "Invalid result of division")
        self.assertEqual(calc.calculate("div", 4, -2), -2, "Invalid result of division")
        self.assertEqual(calc.calculate("div", -4, -2), 2, "Invalid result of division")
        self.assertEqual(calc.calculate("div", 4, 0.5), 8, "Invalid result of division")
        self.assertEqual(calc.calculate("div", -4, 0.5), -8, "Invalid result of division")
        self.assertRaises(ZeroDivisionError, calc.calculate, "div", 1, 0)

if __name__ == '__main__':
    ut.main()
