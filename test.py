import unittest
from program import sum

class Testsum(unittest.TestCase):
    def test_sum1(self):
        result1 = sum(1,2)
        self.assertEqual(result1, 3)
    def test_sum2(self):
        result2 = sum(0,0)
        self.assertEqual(result2,0)
    def test_sum3(self):
        result3 = sum(2,4)
        self.assertEqual(result3, 6)


if __name__ == '__main__':
    unittest.main()
