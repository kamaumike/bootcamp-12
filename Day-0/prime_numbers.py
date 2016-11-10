def prime_numbers(n):
	"""Generate prime numbers between 0 and n"""
	
	primes = [2,3]

	# Loop through the numbers in descending order
	for i in range(n,1,-1):
		if i % 2 == 0 or i % 3 == 0:
			pass
		else:
			primes.append(i)
			primes.sort()
	return primes
