from fibonacci_sequence import fibonacci
import unittest

class FibonacciTestCase(unittest.TestCase):
	"""Test cases for fibonacci function"""
	
	def test_if_output_is_correct(self):
		self.assertEqual(fibonacci(5), "Your Fibonacci numbers are: %s" % ([0,1,1,2,3]))

	def test_if_input_is_a_list(self):
		self.assertEqual(fibonacci([]), "Only integers are allowed")

if __name__ == '__main__':
	unittest.main()
