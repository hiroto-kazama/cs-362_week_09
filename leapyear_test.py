import unittest
import leapyear

class testleapyear(unittest.TestCase):
    def test_leapyear(self):
        Var = leapyear.isLeapyear(2000)
        self.assertEqual(Var, True)

if __name__ == '__main__':
    unittest.main()