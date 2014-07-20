import unittest
from utils import get_excuse


class UtilsTestCase(unittest.TestCase):

    def test_returns_an_excuse(self):
        assert isinstance(get_excuse(), str)

if __name__ == '__main__':
    unittest.main()
