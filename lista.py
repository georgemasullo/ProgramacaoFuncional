from random import *
#01
lista1=range(1,32,2)
print lista1
print"-------"
#02
lista2 =[]

for i in range(ord('a'), ord('p')+1):
    lista2.append(chr(i))
print lista2
print"-------"
#03
lista3=lista1+lista2
print lista3
print"-------"
lista3=lista2+lista1
print"-------"
print lista3
print"-------"
#04
l4 = []
for i in xrange (0,len(lista2)):
	l4 = l4 + [lista1[i]] + [lista2[i]]
	#l4 = l4 + lista1 [len(lista2):]

print l4
print"-------"
#05
i=0
while i<5:
	print l4[i] 
	i=i+1
print"-------"
#06
i=len(l4)-1
while i>=(len(l4)-5):
	print l4[i]
	i=i-1
#07
x="Universidade Estadual do Ceara"
a=x.split()
a[1]="Federal"
x='  '.join(a)
print x
print"-------"
#08
r=[randint(50,100)]
print r
print"-------"
#8a
n=5
i=0
r=[]
while i<n:
	r=r+[randint(50,100)]
	i=i+1
print r
print"-------"
#8b
i=0
while i<len(r):
	if r[i]%3==0:
		r.remove(r[i])
	i=i+1
print r
#8c
print len(r)
#8d
print max(r)
#8e
print min(r)
#8f
r.sort()
print r
#8g
r.sort(reverse=True)
print r
#8h
i=0
aux=[]
while i<len(r):
	if r[i]%2==0:
		aux=aux+[r[i]]
	i=i+1
if aux==[]:
	print "nao tem par"
else:
	print max(aux)
