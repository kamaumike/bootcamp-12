def prime_numbers(n):
	"""Generate prime numbers between 0 and n"""

	primes = []

	if type(n) != int:
		return "Only integers are allowed"
	elif n < 0:
		return "Only postive integers are allowed"
	elif n == 0:
		return "%d is not a prime number" % (0)
	elif n == 1:
		return "%d is not a prime number" % (1)	
	elif n == 2:
		return "%d is a prime number" % (2)
	elif n == 3:
		return "%d is a prime number" % (3)
	else:
		# Loop through the numbers
		for num in range(2, n+1):
			# Loop through the numbers up to num
			for i in range(2, num):
				# Divide num by each number
				if num % i == 0:
					break
			else:
				# Append the number to the primes list
				primes.append(num)				
	return primes
