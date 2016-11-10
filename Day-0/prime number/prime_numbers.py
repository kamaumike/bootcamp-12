def prime_numbers(n):
	"""Generate prime numbers between 0 and n"""

	primes = [2,3]

	if type(n) != int:
		return "Only integers are allowed"
	elif n == 0:
		return "%d is not a prime number" % (0)
	elif n == 1:
		return "%d is not a prime number" % (1)	

	# Loop through the numbers in descending order
	for i in range(n,1,-1):
		if i % 2 == 0 or i % 3 == 0:
			pass
		else:
			primes.append(i)
			primes.sort()
	return primes
