from random import *
#01
print "q-01"
def n_aleatorio(n):
	return [randint(-n,n)for i in range (n) ]
print (n_aleatorio(5))
#02
print "q-02"
n=20
l=n_aleatorio(n)
print l
print l[0]
print l[1]
print l[-1]
print l[:(n-2)]
print l[2:3]
#03
print "q-03"
m=[2,1,4]
def ordenado(n):
	if n[0]<n[1]:
		return True
	else:
		ordenado(n[1:])
	return False

print m
print ordenado(m)
#04
print "q-04"
def divi_por3(n):
	return [i for i in n if i%3==0]
m=[1,2,3]
print divi_por3(m)
#05
print "q-05"
def divi_por5(n):
	return [i for i in n if i%5==0]
m=[5,4,3,2,1]
print divi_por5(m)
#06
print "q-06"
def divi_nem5e3(n):
	return [i for i in n if i%3!=0 and i%5!=0]
print divi_nem5e3(m)
#07
print "q-07"
def fibonacci(n):
	if n<=1:
		return n
	else:
		return fibonacci(n-1)+fibonacci(n-2)
print fibonacci(3)
#08
print "q-08"
def e_primo(n):
	for i in range(2,n):
		if n%i==0 and i!=n:
			return False
	return True
print e_primo(11)
#09
print "q-09"
l=[1,2,3,4,5,6]
def primos(n):
	return [i for i in n if e_primo(i)==True]
print primos(l)
#10
print "q-10"
n=[0,1,2,3]

def partes(n,ini):
	if len(n)-1==ini:
		return [(repeticao(0,n,n[ini]))]
	return [(repeticao(0,n,n[ini]))]+partes(n,ini+1)
def repeticao(ini,n,num):
	if ini<=len(n):
		print n
		print ini
		return [(num,n[0])] +repeticao(ini+1,n[1:],num)
	print n
	print ini
	return [(num,n[0])]
print len(n)
print partes(n,0)
