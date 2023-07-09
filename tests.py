import unittest
import source.calc as calc


class calcTest(unittest.TestCase):
    def test_calc_from_string(self):
        self.assertEqual(str(calc.calc_from_string("1")), "1")
        self.assertEqual(str(calc.calc_from_string("2**10")), "1024")
        self.assertNotEquals(str(calc.calc_from_string("0/0")), "0")



if __name__ == '__main__':
    unittest.main()
