import prime_numbers
import unittest

class PrimeNumberTestCase(unittest.TestCase):
	
	def test_if_input_is_an_integer(self):
		self.assertEqual(prime_numbers.prime_numbers(""), "Only integers are allowed")

	def test_if_input_is_equal_to_zero(self):
		self.assertEqual(prime_numbers.prime_numbers(0), "%d is not a prime number" % 0)

	def test_if_input_is_equal_to_one(self):
		self.assertEqual(prime_numbers.prime_numbers(1), "%d is not a prime number" % 1)

	def test_if_output_is_a_list(self):
		self.assertEqual(type(prime_numbers.prime_numbers(5)), list)

	def test_if_input_is_a_negative_number(self):
		self.assertEqual(prime_numbers.prime_numbers(-1), "Only postive integers are alowed")

if __name__ == '__main__':
	unittest.main()
