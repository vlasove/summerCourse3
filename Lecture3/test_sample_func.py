import sample_func   as sf
import unittest
from program2 import Auto

class TestSample_Func(unittest.TestCase):
    def test_add(self):
        self.assertEqual(sf.add(2,3),5)
        self.assertEqual(sf.add(2,0), 2)
        self.assertEqual(sf.add(-2,-4), -6)
    def test_div(self):
        pass
    def test_sub(self):
        pass
    def test_mult(self):
        pass
    def test_auto(self):
        a = Auto(1,1)
        self.assertEqual(a.horse_power(), 1000)
    
if __name__ == "__main__":
    unittest.main()


