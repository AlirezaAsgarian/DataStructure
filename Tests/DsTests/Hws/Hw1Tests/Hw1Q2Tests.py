
import unittest
import DsHws.Hw1.dsHw2Q1


class main_test(unittest.TestCase):
    def test_number_of_halat(self):
        self.assertEqual(7, DsHws.Hw1.dsHw2Q1.number_of_halat(value=48))
        self.assertEqual(3, DsHws.Hw1.dsHw2Q1.number_of_halat(value=24))
        self.assertEqual(2, DsHws.Hw1.dsHw2Q1.number_of_halat(value=20))

    def test_binary_search(self):
        self.assertEqual(48, DsHws.Hw1.dsHw2Q1.getResult(7))
        self.assertEqual(24, DsHws.Hw1.dsHw2Q1.getResult(3))
        self.assertEqual(-1, DsHws.Hw1.dsHw2Q1.getResult(10))