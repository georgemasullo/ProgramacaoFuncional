def cons(x,xs=None):
	return(x,xs)
def lista(*xs):
	if not xs:
		return None
	return cons(xs[0],lista(*xs[1:]))
def head(xs):
	return xs[0]
def tail(xs):
	return xs[1:]
def is_empty(xs):
	return xs is None
def last(xs):
	if is_empty(tail(xs)):
		return cons(head(xs))
	return last(tail(xs))
def concat(xs,yx):
	if is_empty(xs):
		return ys
	return cons( head(xs),concat(tail(xs),ys) )
def reverse(xs):
	if is_empty(xs):
		return xs
	return concat( reverse(tail(xs)),cons(head(xs)) )
a=lista(1,2,3,4,5,6)
print lista(a)
def tupla(x,xs):
	return xs[x]
def item(n,x):
	return x[n] 
def neg(n):
	if n<0:
		return n
	return -n
def take(n,xs):#trocar nome
	if n==1:
		return xs[0]
	return (take(n-1,xs),item(0,tupla(n-1,xs)))
print take(2,a)

def drop(n,xs):#trocar nome
	print "aa", xs
	if n==1:
		return xs[0]
	return ( xs[0] ,drop(n-1,tupla(-1,xs)) )
print drop(3,reverse(a))
	
