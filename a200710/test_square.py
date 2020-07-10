import unittest
from square import square

class TestMysquare(unittest.TestCase):
  def test_square(self):
    self.assertEqual(square(3), 9)
    self.assertEqual(square(1), 1)
    self.assertEqual(square(-3), 9)
    self.assertEqual(square(0), 0)

if __name__ == '__main__':
  unittest.main()
    
