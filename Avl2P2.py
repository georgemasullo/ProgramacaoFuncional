#01
print "----------------q-01----------------"
def islice(i,x):
	return iter(i[:x])
print list(islice('ABCDEFGHIJ', 1))
#02
print "----------------q-02----------------"
def islice2(i, x, p):
	return iter(i[x:p])
print list(islice2('ABCDEFGHIJ', 1,3))
#03
print "----------------q-03----------------"
def islice3(i, x, p, u):
	def aux(l,x):
		return l[x]
	if x<=p:
		return iter(list(aux(i, x)) + list(islice3(i, x+u, p, u)))
	return iter(i[x:p])
print list(islice3('ABCDEFGHIJ', 0,8,2))
#04
print "----------------q-04----------------"
def permutations(i, r):
	if r>0:
		return iter([ i[0]+x for x in i  if i[0]!=x] + list(permutations(i[1:],r-1)) )
	return [i[0]+x for x in i if i[0]!=x]
print list(permutations('ABCD', 2))
#05
print "----------------q-05----------------"
def product(*iterables):
	if not iterables:
		return
	for i in iterables[0]:
		for t in map(tuple,iterables):
			for k in t:
				if(not i in t):
					yield [i,k]

print list(product('ABCD', 'xy','10','MN'))

#06
print "----------------q-06----------------"
def repeat(x, n):
	if n>1:
		return iter([x] +list(repeat(x,n-1)))
	return [x]
print list(repeat(10, 2))
#07
print "----------------q-07----------------"
def starmap(function, iterable):
	return iter([ function(*i) for i in iterable ])
print list(starmap(pow, [(2,5), (3,2), (10,3)]))
print "----------------q-08----------------"
#08
def takewhile(predicate, iterable):
	return iter( [ i for i in iterable if predicate(i) ] )
print list(takewhile(lambda x: x<5, [1,4,6,4,1]))
print "----------------q-09----------------"
#09
def tee(iterable, n=2):
	return iter([( i for i in iterable ) for x in range(n)])
a,b,c = tee("ABCDEFGHIJ",3)
print a.next()
print a.next()
print b.next()
print c.next()
print b.next()
print a.next()
print "----------------q-10----------------"
#10
def zip_longest(f=None,*i):
	def maxi(l,i=0,j=0):
		if len(l)-1==i:
			if len(l[i])>=len(l[j]):
				return i
			elif len(l[i])<len(l[j]):
				return j
		else:
			if len(l[i])>=len(l[j]):
				return maxi(l,i+1,i)
			elif len(l[i])<len(l[j]):
				return maxi(l,i+1,j)
	def aux(i,ma,f,x=0):
		if len(i)-1==x:
			return [ list(i[x]) +[f for k in range(ma - len(i[x]))] ]
		return [list(i[x]) +[f for k in range(ma - len(i[x]) )]] + aux(i,ma,f,x+1)
	def iterc(l,tam):
		return [[ i[x] for i in [k for k in l] ] for x in range(tam)]
	def uni(l):
		if len(l)==1:
			return str(l[0])
		return str(l[0])+uni(l[1:])
	return ([uni(iterc(aux(i,len(i[maxi(i)]),f),len(i[maxi(i)]))[k]) for k in range(len(i[maxi(i)])) ])
print list(zip_longest( '-','ABCD', 'xy'))
