import unittest
from business.calculate_magic_numbers import CalculateMagicNumbers

class TestCalculateMagicNumbers(unittest.TestCase):

    #### VALID RESULTS
    def test_calculate_magic_numbers(self):
        init = 8
        end = 27
        magic_number = CalculateMagicNumbers()
        self.assertEqual(magic_number.calculate(init, end), 2)

    def test_is_magic_number(self):
        magic_number = CalculateMagicNumbers()
        self.assertEqual(magic_number.isMagicNumber(9), True)

    def test_is_prime(self):
        magic_number = CalculateMagicNumbers()
        self.assertEqual(magic_number.isPrime(3), True)

    def test_is_square(self):
        magic_number = CalculateMagicNumbers()
        self.assertEqual(magic_number.haveSquare(100), True)

    #### INVALID RESULTS
    def test_is_not_magic_number(self):
        magic_number = CalculateMagicNumbers()
        self.assertEqual(magic_number.isMagicNumber(100), False)

    def test_is_not_prime(self):
        magic_number = CalculateMagicNumbers()
        self.assertEqual(magic_number.isPrime(10), False)

    def test_is_not_square(self):
        magic_number = CalculateMagicNumbers()
        self.assertEqual(magic_number.haveSquare(10), False)

if __name__ == '__main__':
    unittest.main()