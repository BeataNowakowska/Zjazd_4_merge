import unittest

from zamien_lib import zamien_jedna


class MyTestCase(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(zamien_jedna(0), "zero")

    def test_jeden(self):
        self.assertEqual(zamien_jedna(1),"jeden")

    def test_minusjeden(self):
        self.assertEqual(zamien_jedna(-1),"minus jeden")


if __name__ == '__main__':
    unittest.main()

