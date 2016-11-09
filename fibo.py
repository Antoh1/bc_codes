def fibo(n):
	if n<=1:
		return n
	fib = fibo(n-1) + fibo(n-2)
	return fib	
print fibo(10)	