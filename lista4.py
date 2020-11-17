def soma():
	return sum([i**2 for i in range(0,100) ])
print soma()
def pi(n):
	return (float) ( sum([((-1)**i)/(2*i+1) for i in range(0,n) ]) )
print pi(3)
