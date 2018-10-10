import unittest
from business.total_magic_numbers import TotalMagicNumbers

class TestCountMagicNumbers(unittest.TestCase):

    def test_count_magic_numbers(self):
        data = [[8,27], [49, 49]]
        total = TotalMagicNumbers()
        self.assertEqual(total.calculate(data), 3)
    

if __name__ == '__main__':
    unittest.main()