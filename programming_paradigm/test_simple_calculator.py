import unittest
from simple_calculator import SimpleCalculator # type: ignore

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        # Set up an instance of SimpleCalculator for use in the tests
        self.calc = SimpleCalculator()

    def test_addition(self):
        # Test addition
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_subtraction(self):
        # Test subtraction
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(-3, 2), -5)

    def test_multiplication(self):
        # Test multiplication
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(0, 100), 0)

    def test_division(self):
        # Test division
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-6, 2), -3)
        self.assertEqual(self.calc.divide(0, 5), 0)
        
        # Test division by zero
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)

# Run the tests
if __name__ == "__main__":
    unittest.main()
