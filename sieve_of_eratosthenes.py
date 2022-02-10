def sieve_of_erosthenes(n):
	prime_list = [] #Creates an empty list
	for i in range (2, n+1): #For loop iterates through 1st prime (2) up to and including n
		if i not in prime_list: #Condition check: detects numbers that should be printed
			print(i) #Prints a prime factor
			for j in range (i*i, n+1, i): #For loop iterating from i*i up to and including n every +i
				prime_list.append(j) #Adds all numbers multiples of a prime factor -> loop restarts 

print(sieve_of_erosthenes(10000))
