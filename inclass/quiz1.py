

def filter_out_negative_numbers(inputList):

	finalList = [];

	for i in inputList:

		if i >= 0:
			finalList.append(i)

	return finalList

#filter_out_negative_numbers([-2.0, 5, 10, -100, 5])

def in_language(word):

	if word == '':
		return True

	numA = 0
	numB = 0

	
	for i in word:

		if i == 'a':
			numA += 1
			print numA

		elif i == 'b':
			numB += 1

		else:
			return False

	if numA == numB:
		return True
	else:
		return False

#print in_language('aaabb')



def fib(n):

	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

for i in range (0,10):
	print fib(i)


