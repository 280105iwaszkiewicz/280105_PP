import unittest
from PP1_280105_calculator import Add

class TestAdd(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(Add(""), 0)

    def test_1(self):
        self.assertEqual(Add("1"), 1)

    def test_2(self):
        self.assertEqual(Add("1,2"), 3)

    def test_wiele(self):
        self.assertEqual(Add("1,2,3"), 6)

    def test_n(self):
        self.assertEqual(Add("1\n2,3"), 6)

    def test_literka(self):
        with self.assertRaises(ValueError):
            Add("1,a")

    def test_zly_format(self):
        with self.assertRaises(ValueError):
            Add("1,\n")

    def test_przecinki(self):
        with self.assertRaises(ValueError):
            Add("1,,2")


if __name__ == "__main__":
    unittest.main()