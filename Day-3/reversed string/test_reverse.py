import unittest

from reverse import reverse_string

class ReverseStringTest(unittest.TestCase):
    """docstring for ReverseStringTest"""

    def test_empty_string(self):
        self.assertIsNone(reverse_string(''),
                          msg='should return `None` for empty string')

if __name__ == '__main__':
    unittest.main()