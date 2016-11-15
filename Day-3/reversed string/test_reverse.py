import unittest

from reverse import reverse_string

class ReverseStringTest(unittest.TestCase):
    """docstring for ReverseStringTest"""

    def test_empty_string(self):
        self.assertIsNone(reverse_string(''),
                          msg='should return `None` for empty string')

    def test_palidromes1(self):
        self.assertTrue(
            reverse_string('anna'),
            msg='should return true for `anna`'
        )

    def test_palidromes2(self):
        self.assertTrue(
            reverse_string('NaN'),
            msg='should return true for `NaN`'
        )        

    def test_palidromes3(self):
        self.assertTrue(
            reverse_string('civic'),
            msg='should return true for `civic`'
        )

    def test_non_palidromes1(self):
        self.assertEqual(
            'skoob',
            reverse_string('books'),
            msg='should return `skoob` for `books`'
        )                

if __name__ == '__main__':
    unittest.main()