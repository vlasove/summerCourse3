import unittest
import equation as eq

class TestSample_Func(unittest.TestCase):
    def test_linear(self):
        self.assertEqual(eq.linear(1,1),-1)  #B*x+C = 0
        self.assertEqual(eq.linear(1,0), 0)
        self.assertEqual(eq.linear(0,-4),"нет решений!")
    def test_poly(self):
        self.assertEqual(eq.poly(1,2,1), -1)
        
    
    
if __name__ == "__main__":
    unittest.main()
