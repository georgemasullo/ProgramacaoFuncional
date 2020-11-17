from random import *
import math
#01
print "--------------------q-01--------------------"
#a
print "--------------------A--------------------"
l=[]
def divi(n,lista):
	if n==1:
		return 1
	if filter(lambda x:n%x==0,lista)[0]==1:
		return filter(lambda x:n%x==0,lista)[1]
	return filter(lambda x:n%x==0,lista)[0]
def primo(n):
	if divi(n,xrange(1,n+1))==n:
		return True
	return False
def Nprimos(n,p=1):
	if primo(p) and n==1:
		return [p]
	if primo(p):
		return [p]+Nprimos(n-1,p+1)
	return Nprimos(n,p+1)
l=Nprimos(15)
print l
#b
print "--------------------B--------------------"
def Nletras(n,p='a'):
	if n>26:
		return null
	if n==1:
		return [p]
	return [p]+ Nletras(n-1,chr(ord(p)+1))
a=Nletras(15)
print a
#c
print "--------------------C--------------------"
def concat(a,b):
	return a+b
print concat(a,l)
print concat(l,a)
#d
print "--------------------D--------------------"
def inter(a,b):
	if len(a)==1 and len(b)==1:
		return [a[0]] + [b[0]]
	if len(a)==len(b):
		return [a[0]]+[b[0]]+inter(a[1:],b[1:])
	if len(a)>0 and len(b)==0:
		return a[0]+inter(a[1:],b[1:])
	return b[0]+inter(a[1:],b[1:])
print inter(a,l)
#e
print "--------------------E--------------------"
def Nprimeiros(n,l):
	if len(l)>= n:
		if n==1:
			return l[0]
		return l[0:n]
	return None
print Nprimeiros(5,a)
#f
print "--------------------F--------------------"
def Nultimos(n,l):
	if len(l)>= n:
		if n==1:
			return [l[-1]]
		return l[-1:]+Nultimos(n-1,l[0:-1])
	return [None]
print Nultimos(5,a)
#02
print "--------------------q-02--------------------"
def trocarPalavra(f,i,p):
	def subs(a,p,i):
		if len(a)-1==i:
			return subs(a[0:-2],p,i)+[p]
		if len(a)==1:
			return [a[0]]
		return	subs(a[0:-1],p,i)+[a[-1]]
	return ' '.join(subs(f.split(),p,i))
print trocarPalavra("Universidade Estadual do Ceara",2,"Federal")	
#03
print "--------------------q-03--------------------"
n=randint(1,50)
#a
print "--------------------A--------------------"
def n_aleatorio(n):
	return [randint(-n,n)for i in range (n) ]
n=n_aleatorio(n)
print n
#b
print "--------------------B--------------------"
def remove_divi_por3(n):
	if len(n)==1 and n[0]%3!=0:
		return [n[0]]
	elif len(n)==1 and n[0]%3==0:
		return []
	elif n[0]%3!=0:
		return [n[0]]+remove_divi_por3(n[1:])
	else:
		return remove_divi_por3(n[1:])
n=remove_divi_por3(n)
print n
print "--------------------C--------------------"
n.remove(max(n))
print n
print "--------------------D--------------------"
n.remove(min(n))
print n
print "--------------------E--------------------"
print len(n)
print "--------------------F--------------------"
n.sort()
print n
print "--------------------G--------------------"
n.sort(reverse=True)
print n
#04
print "--------------------q-04--------------------"

def n_aleatorio(n):
	return [randint(-n,n)for i in range (n) ]
x=10
n=n_aleatorio(x)
print n
print "--------------------A--------------------"
print n[0]
print "--------------------B--------------------"
print n[1:]
print "--------------------C--------------------"
print n[-1]
print "--------------------D--------------------"
print n[:(x-2)]
print "--------------------E--------------------"
print n[2:3]
#05
print "--------------------q-05--------------------"
m=[2,1,2,3,5,4]
print m
print "--------------------A--------------------"
def ordenado(n):
	if n[0]<n[1]:
		return True
	else:
		ordenado(n[1:])
	return False
print ordenado(m)
print "--------------------B--------------------"
def divi_por3(n):
	return [i for i in n if i%3==0]
print divi_por3(m)
print "--------------------C--------------------"
def divi_por5(n):
	return [i for i in n if i%5==0]
print divi_por5(m)
print "--------------------D--------------------"
def divi_nem5e3(n):
	return [i for i in n if i%3!=0 and i%5!=0]
print divi_nem5e3(m)
#06
print "--------------------q-06--------------------"
def fibonacci(n):
	if n<=1:
		return n
	else:
		return fibonacci(n-1)+fibonacci(n-2)
print fibonacci(3)
#07
print "--------------------q-07--------------------"
def e_primo(n):
	for i in range(2,n):
		if n%i==0 and i!=n:
			return False
	return True
print e_primo(11)
#08
print "--------------------q-08--------------------"
l=[1,2,3,4,5,6]
def primos(n):
	return [i for i in n if e_primo(i)==True]
print primos(l)


#10
print "--------------------q-10--------------------"
def somatorio(numeros):
	if len(numeros)==0:
		return 0
	return numeros[0]+somatorio(numeros[1:])
def filtra(lista,filtro,ini=0):
	if ini== len(lista):
		return []
	if filtro(lista[ini]):
		return [lista[ini]] + filtra(lista,filtro,ini+1)
	else:
		return filtra(lista,filtro,ini+1)
l=[1,2,3,4]
n=2
print "--------------------A--------------------"
print somatorio(filtra(l,lambda v:v%n==0))
print "--------------------B--------------------"
print somatorio(filtra(l,lambda v:n%v==0))
print "--------------------C--------------------"
print somatorio(filtra(l,lambda v:v>=n))
print "--------------------D--------------------"
def mdc(m,n):
	if m==0:
		return n
	if m>0:
		return mdc((n%m),m)
	return None
def primosEntreSi(x,y):
	if mdc(x,y)==1:
		return True
	return False
print somatorio(filtra(l,lambda v:mdc(v,n)==1))
#11
print "--------------------q-11--------------------"
def coefiente_Binimial(n,k):
	def fatorial(n): 
   		if n<=1: 
      			return 1
   		else: 
	 		return n*fatorial(n-1)
	return fatorial(n)/(fatorial(k)*fatorial(n-k))
print coefiente_Binimial(4,3) 
#12
print "--------------------q-12--------------------"
def triangulo_pascal(ini,n):
	def repeticao(ini,n,num):
		if ini==n:
			return [(num,ini)]
		return [(num,ini)] +repeticao(ini+1,n,num)
	if ini==n:
		return [(repeticao(0,n,ini))]
	return [(repeticao(0,ini,ini))]+triangulo_pascal(ini+1,n)

print triangulo_pascal(0,2)
#13

#14
print "--------------------q-14--------------------"
def soma():
	return sum([i**2 for i in range(0,100) ])
print soma()
#15
print "--------------------q-15--------------------"
print "--------------------A--------------------"
def pi(n):
	return (sum([((-1)**i)/((2.0*i)+1) for i in range(n+1)]))*4
print pi(1000)
print "--------------------q-B--------------------"
def pi2(n):
	return (sum([ ( ( (-1.0)**i)/ ((i+1)**2) ) for i in range(n+1) ]) )*12
print pi2(1000)
print "--------------------C--------------------"
print pi(10)
print pi(100)
print pi(1000)
print pi2(10)
print pi2(100)
print pi2(1000)
#16
print "--------------------q-16--------------------"
def divip(n):
	return [i for i in range(1,n) if n%i==0]
print divip(6)
#17
print "--------------------q-17--------------------"
def ehnatural(n):
	if sum(divip(n))==n:
		return True
	return False
print ehnatural(9)
#18
print "--------------------q-18--------------------"
def knatural(n,x=1):
	if n==1 and ehnatural(x):
		return [x]
	elif n>1 and ehnatural(x):
		return [x]+knatural(n-1,x+1)
	else:
		return knatural(n,x+1)
print knatural(3)
#19
print "--------------------q-19--------------------"
l=n_aleatorio(10)
print l
#A
print "--------------------A--------------------"
print l[1]
print "--------------------B--------------------"
print l[-1]
print "--------------------C--------------------"
print l[1:]
print "--------------------D--------------------"
print l[:5] + [11,12] + l[5:]
print "--------------------E--------------------"
print l.sort()

#21
print "--------------------q-21--------------------"
x=[1,2,3]
print x
print "--------------------A--------------------"
def maior_que_primeiro(x):
	return [i for i in x if i>x[0] ]
print maior_que_primeiro(x)
print "--------------------B--------------------"
def menores_que_media(x):
	return [i for i in x if i<sum([e for e in x])/len(x)]
print menores_que_media(x)
print "--------------------C--------------------"
def qP(l):
	return[i for i in l if math.sqrt(i)**2 ==i ]
print qP([1,2,3,4,5,6,7,8,9])
print "--------------------D--------------------"
def lPerf(l):
	return[i for i in l if ehnatural(i)==True]
print lPerf([1,2,3,4,5,6,7,8,9,10,11,12,13])
print "--------------------E--------------------"
def ListaPrimos(l):
	return [i for i in l if e_primo(i)]
print ListaPrimos([1,2,3,4,5,6,7,8,9,10,11])
#22
print "--------------------q-22--------------------"
def const(x,xs=None):
	return(x,xs)
def listar(*xs):
	if not xs:
		return None
	return const(xs[0],listar(*xs[1:]))
def head(xs):
	return xs[0]
def tail(xs):
	return xs[1:]
def is_empty(xs):
	return xs is None
def last(xs):
	if is_empty(tail(xs)):
		return const(head(xs))
	return last(tail(xs))
def concat(xs,yx):
	if is_empty(xs):
		return ys
	return const( head(xs),concat(tail(xs),ys) )
def reverse(xs):
	if is_empty(xs):
		return xs
	return concat( reverse(tail(xs)),const(head(xs)) )
#a
def take(n,xs):
	if n>1 and xs[1] is None:
		return [xs[0]]#+["Passou limite de tamanho"]
	elif n==1 and xs[0] != None:
		return [xs[0]]
	return [xs[0]]+take(n-1,xs[1])
#a=const(5)
#a=const(7,a)
#a=const(8,a)
#a=const(9,a)
a=listar(5,7,8,9)
print a
print "--------------------A--------------------"
print take(4,a)
print "--------------------C--------------------"
def select(n,xs):
	if n>1 and xs[1] is None:
		return "indice nao existe"
	elif n==1 and xs[0] != None:
		return xs[0]
	return select(n-1,xs[1])
print select(4,a)
print "--------------------D--------------------"
def pop(xs):
	if xs[1] is None:
		return None
	return const(xs[0],pop(xs[1]))
print pop(a)
print "--------------------F--------------------"
def find(n,xs,cont=0):
	if n!=x[0] and xs[1] is None:
		return None
	elif n==xs[0]:
		return cont
	return find(n,xs[1],cont+1)
print find(8,a)

#23
print "--------------------q-23--------------------"
def inserir(x,esq=None,dire=None):
	return(x,esq,dire)
def lista(*xs):
	if xs is None:
		return None
	return (xs[0],lista(xs[1]),lista(xs[2]))
def con(raiz,valor):
	if raiz is None:
		return inserir(valor)
	elif valor<raiz[0]:
		return (raiz[0],con(raiz[1],valor),raiz[2])
	elif valor>raiz[0]:
		return (raiz[0],raiz[1],con(raiz[2],valor))
	else:
		return raiz
def busca(raiz,valor):
	if raiz is None:
		return None
	elif valor==raiz[0]:
		return raiz[0]
	elif valor<raiz[0]:
		return busca(raiz[1],valor)
	else:
		return busca(raiz[2],valor)
#24
print "--------------------q-24--------------------"
listar=[1,2,3,4,5,6,7,8,9,10,11,12]
n=3
print "--------------------A--------------------"
#a
print filter(lambda x:x%n==0,listar)
#b
print "--------------------B--------------------"
print filter(lambda x:n%x==0,listar)
print "--------------------C--------------------"
print filter(lambda x:primosEntreSi(n,x),listar)

#26
print "--------------------q-26--------------------"

#28
print "--------------------q-28--------------------"
	
def cr(texto):
	def inserir(x,q=1):
		return[(x,q)]
	def con(raiz,valor):
		if raiz is None:
			return inserir(valor)
		elif valor==raiz[0][0]:
			return raiz[1:]+inserir(raiz[0][0],raiz[0][1]+1)
		else:
			return raiz+inserir(valor)

	if len(texto)==1:
		return con(None,texto[0])
	return con(cr(texto[1:]),texto[0])
	
print cr("banana")
#29
print "--------------------q-29--------------------"

def intersperce(simb,frase):
	if len(frase)==1:
		return frase[0]
	return frase[0]+simb+intersperce(simb,frase[1:])
print intersperce('-', "banana")
#30
print "--------------------q-30--------------------"
def nub(texto):
	def reves(l):
		if len(l)==1:
			return [l[0]]
		return [l[-1]]+reves(l[:-1])
	def soLetras(texto):
		return [l for l in ([i[0] for i in reves(cr(texto))])]
	def e(texto):
		if len(texto)==1:
			return texto[0]
		return texto[0]+e(texto[1:])
	return e(soLetras(texto))
print nub("banana")
#37
print "--------------------q-31--------------------"
print "--------------------A--------------------"
def encripta(palavra,chave):
	if palavra[0]>='a' and palavra[0]<='z':
		if len(palavra)==1:
			return chr((((ord(palavra[0])- ord ('a')+chave)%26)+ord('a')))
		return chr((((ord(palavra[0])- ord ('a')+chave)%26)+ord('a')))+encripta(palavra[1:],chave)
	elif palavra[0]>='A' and palavra[0]<='Z':
		if len(palavra)==1:
			return chr((((ord(palavra[0])- ord ('A')+chave)%26)+ord('A')))
		return chr((((ord(palavra[0])- ord ('A')+chave)%26)+ord('A')))+encripta(palavra[1:],chave)
print encripta("banana",2)
#38
def diferenca_nivel(arv,valor=0):
	if arv[1] is None and arv[2] is None:
		return valor
	elif arv[1] is not None and arv[2] is None:
		return diferenca_nivel(arv[1],valor+1) - 0
	elif arv[1] is None and arv[2] is not None:
		return diferenca_nivel(arv[2],valor+1) - 0
	else:
		return diferenca_nivel(arv[1],valor+1) - diferenca_nivel(arv[2],valor+1)
print "--------------------q-38--------------------"
a=con(None,10)
a=con(a,5)
a=con(a,15)
a=con(a,16)
a=con(a,9)
a=con(a,6)
print a
print diferenca_nivel(a)
#39
print "--------------------q-39--------------------"
def isBanl(arv):
	if diferenca_nivel(arv)==1:
		return True
	else:
		return False
print isBanl(a)
