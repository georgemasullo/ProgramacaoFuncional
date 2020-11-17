#03
def maior_que_primeiro(x):
	return [i for i in x if i>x[0] ]
x=[1,2,3]
print maior_que_primeiro(x)
def b(x):
	return [i for i in x if i<sum([e for e in x])/len(x)]
print b(x)

#04
print (100,2,3,4)[0]
