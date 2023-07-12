import unittest
import source.calc as calc


class calcTest(unittest.TestCase):
    def test_calc_1(self):
        self.assertEqual(str(calc.calc_from_string("1")), "1")

    def test_calc_2(self):
        self.assertEqual(str(calc.calc_from_string("2**10")), "1024")

    def test_calc_3(self):
        self.assertNotEqual(str(calc.calc_from_string("0/0")), "0")

    def test_calc_4(self):
        self.assertEqual(str(calc.calc_from_string("0.1 + 0.3 * e ** pi")), "7.042207789833778")


if __name__ == '__main__':
    unittest.main()
