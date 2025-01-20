import unittest
from simple_calculator import SimpleCalculator # type: ignore

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        # Set up an instance of SimpleCalculator for use in the tests
        self.calculator = SimpleCalculator()

    def test_add(self):
        # Test addition
        self.assertEqual(self.calculator.add(2, 3), 5)
        self.assertEqual(self.calculator.add(-1, 1), 0)
        self.assertEqual(self.calculator.add(-2, -3), -5)

    def test_subtract(self):
        # Test subtraction
        self.assertEqual(self.calculator.subtract(5, 3), 2)
        self.assertEqual(self.calculator.subtract(-1, -1), 0)
        self.assertEqual(self.calculator.subtract(-3, 2), -5)

    def test_multiply(self):
        # Test multiplication
        self.assertEqual(self.calculator.multiply(2, 3), 6)
        self.assertEqual(self.calculator.multiply(-1, 5), -5)
        self.assertEqual(self.calculator.multiply(0, 100), 0)

    def test_divide(self):
        # Test division
        self.assertEqual(self.calculator.divide(6, 3), 2)
        self.assertEqual(self.calculator.divide(-6, 2), -3)
        self.assertEqual(self.calculator.divide(0, 5), 0)
        
        # Test division by zero
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(5, 0)

# Run the tests
if __name__ == "__main__":
    unittest.main()
