import operator
def delslice(colecao, i, f):
	return operator.concat(colecao[:i],colecao[f+1:])
print "--------01---------"
print delslice([0,1,2,3,4,5,6,7,8,9],4,7)

def getslice(colecao, i, f):
	return colecao[i:f+1]
print "--------02---------"
print getslice([0,1,2,3,4,5,6,7,8,9],4,7)

def setslice(alvo, i, f, fonte):
	if f-i>=len(fonte):
		return operator.concat(operator.concat(alvo[:i],fonte),alvo[f+1:])
	return operator.concat(operator.concat(alvo[:i],fonte[:(f-i)+1]),alvo[f+1:])

print "--------03---------"
print setslice([0,1,2,3,4,5,6,7,8,9],4,7,[10,11,12,13,14,15,26,27])

def iadd(a,b):
	return operator.add(a,b)
print "--------04---------"
print iadd(1,2)

def imul(a,b):
	return operator.mul(a,b)
print "--------05---------"
print imul(2,2)

def ipow(a,b):
	return pow(a,b)
print "--------06---------"
print ipow(3,2)

def imod(a,b):
	return operator.mod(a,b)
print "--------07---------"
print imod(1,2)

def isub(a,b):
	return operator.sub(a,b)
print "--------08---------"
print isub(5,2)

def idiv(a,b):
	return operator.truediv(a,b)
print "--------09---------"
print idiv(3,2)

def ifloor(a,b):
	return operator.floordiv(a,b)
print "--------10---------"
print ifloor(3,2)
