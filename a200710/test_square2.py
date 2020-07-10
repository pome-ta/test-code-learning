import unittest
from square2 import square2

class TestMysquare(unittest.TestCase):
  def test_square2(self):
    self.assertEqual(square2(3), 9)
    self.assertEqual(square2(1), 1)
    self.assertEqual(square2(-3), 9)
    self.assertEqual(square2(0), 0)

if __name__ == '__main__':
  unittest.main()
    
