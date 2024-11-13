import unittest
from unittest.mock import patch

class TestCalculation(unittest.TestCase):

    @patch('src.calculation.Calculation.sum',
           return_value=9)
    def test_sum(self, sum): # test don't pass
        self.assertEqual(sum(5, 3), 8)
    
    @patch('src.calculation.Calculation.sub',
           return_value=7)
    def test_sub(self, sub):
        self.assertEqual(sub(10, 3), 7)
    
    @patch('src.calculation.Calculation.div',
           return_value=3)
    def test_sub(self, div):
        self.assertEqual(div(10, 3), 3)

    @patch('src.calculation.Calculation.mul',
           return_value=15)
    def test_sub(self, mul):
        self.assertEqual(mul(5, 3), 15)
    
    @patch('src.calculation.Calculation.pow2',
           return_value=25)
    def test_sub(self, pow2):
        self.assertEqual(pow2(5), 25)

if __name__ == "__main__":
    unittest.main()