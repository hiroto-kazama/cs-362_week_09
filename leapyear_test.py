import unittest
import leapyear

class testleapyear(unittest.TestCase):
    def test_leapyear(self):
        Var = leapyear.isLeapyear(4000)
        self.assertEqual(Var, False)

if __name__ == '__main__':
    unittest.main()