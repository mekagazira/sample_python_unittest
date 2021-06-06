import unittest
from main import tashizan


class TestTashizan(unittest.TestCase):
    """test class of main.py
    """

    def test_tashizan1(self):
        """test method for tashizan
        """
        value1 = 1
        value2 = 2
        expected = 3
        actual = tashizan(value1, value2)
        self.assertEqual(expected, actual)

    def test_tashizan2(self):
        """test method for tashizan
        """
        value1 = 100
        value2 = 0
        expected = 100
        actual = tashizan(value1, value2)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()