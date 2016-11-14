def fibonacci(n):
	"""Returns a Fibonacci sequence from 0 to n"""

	sequence = [0,1]

	if type(n) != int:
		return "Only integers are allowed"
	# Loop through the numbers 
	for i in range(2,n):
		# Append the numbers to the sequence list
		sequence.append(sequence[i-1] + sequence[i-2])		
	# Return the fibonacci sequence
	return "Your Fibonacci numbers are: %s" % (sequence)
