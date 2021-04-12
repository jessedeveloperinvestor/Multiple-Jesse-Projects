def PrimeOrNot(num):
	if num>1:
		for i in range(2,num):
			if(num%i)==0:
				print(num,'is not a prime number')
				break
			else:
				print(num,'is a prime number')

PrimeOrNot(1)
PrimeOrNot(3)
PrimeOrNot(10)
PrimeOrNot(11)