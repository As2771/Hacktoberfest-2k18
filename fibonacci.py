Python 3.6.5 (v3.6.5:f59c0932b4) on win32

>>> def fib(n):
	if(n == 0):
		return 0
	elif(n == 1):
		return 1
	else:
		return(fib(n-1) + fib(n-2))

	
>>> n = int(input("Enter number of terms: "))
Enter number of terms: 5
>>> for i in range(n):
	print(fib(i))

	
0
1
1
2
3
>>> 
