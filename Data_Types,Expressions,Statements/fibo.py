def fib(b):
	a,n=0,1
	while n<b:
		print(n,end='')
		a,n=n,a+n
def fib2(n):
	result=[]
	a,b=0,1
	while b<n:
		result.append(b)
		a,b=b,a+b
	return result