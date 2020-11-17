#01
listar=[1,2,3,4,5,6,7,8,9,10,11,12]
n=3
#a
print filter(lambda x:x%n==0,listar)
#b
print filter(lambda x:x%n==1,listar)
#c
print filter(lambda x:n%x==0,listar)
#02
def divi(n,lista):
	if n==1:
		return 1
	if filter(lambda x:n%x==0,lista)[0]==1:
		return filter(lambda x:n%x==0,lista)[1]
	return filter(lambda x:n%x==0,lista)[0]
print divi(n,listar)
#03
def primo(n):
	if divi(n,xrange(1,n+1))==n:
		return True
	return False
print primo(4)
#04
print len(listar)
def primos(l):
	if len(l)==1:
		if primo(l[0]) is True:
			return [l[0]]
		else:
			return [None]
	if primo(l[0]) is True:
		return [l[0]] +primos(l[1:])
	else:
		return primos(l[1:])
print primos(listar)
#05
def inserir(x,q=1):
	return(x,q)
def con(raiz,valor):
	if raiz is None:
		return inserir(valor)
	elif valor==raiz[0]:
		return (raiz[0],raiz[1],raiz[2],raiz[3]+1)
	else:
		return raiz+inserir(valor)
		
def cr(texto):
	if len(texto)==1:
		return con(None,texto[0])
	return con(cr(texto[1:]),texto[0])
	
print cr("banana")
#06
#a
#-ord('a') ou --ord('A')
def cifra(texto,k):
	if texto[0]>="a" and texto[0]<="z":
		if(len(texto)==1):
			return [chr( ( (ord(texto[0])- ord('a')) +k) % 26)]
		return chr(((ord(texto[0])-ord('a')) +k) % 26) + cifra(texto[1:],k)
	elif texto[0]>="A" and texto[0]<="Z":
		if(len(texto)==1):
			return [chr( ( (ord(texto[0])- ord('A')) +k) % 26)]
		return chr(((ord(texto[0])-ord('A')) +k) % 26) + cifra(texto[1:],k)
print cifra("a",2)
