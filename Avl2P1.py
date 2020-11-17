import os
import sys
#01
print "----------------q-01----------------"
def reverse(l):
	if len(l)==1:
		return[l[0]]
	else :
		return [l[-1]]+ reverse(l[:-1])
a= iter(reverse([1,2,3]))
print a.next()
print a.next()
print a.next()


#02
print "----------------q-02----------------"
a=open("teste.txt","r")
def linha(arquivo):
	return[i for i in arquivo if len(i)>40]

print linha(a)
#03
print "----------------q-03----------------"
def dire(dire):
	return [root for root, dirs, files in os.walk(dire)]
print dire("/home/george/Documentos")		
#04
print "----------------q-04----------------"
def verificaNome(n):
	if n[-3]=='.'and n[-2]=='p' and n[-1]=='y':
		return True
	return False
#print verificaNome("teste.txt")
def arquivosEmPy(dire):
	return [i for i in os.listdir(dire) if verificaNome(i) ]
print arquivosEmPy("/home/george/Documentos")
def NarquivosEmPy(dire):
	return len([i for i in os.listdir(dire) if verificaNome(i) ])
print NarquivosEmPy("/home/george/Documentos")
#05
print "----------------q-05----------------"
def NLinhas(dire):
	return [len(open (dire+"/"+i,"r").readlines()) for i in os.listdir(dire) if verificaNome(i) ]
print sum(NLinhas("/home/george/Documentos"))
#06
print "----------------q-06----------------"
def olhaLinha(linha):
	if linha[0]=='#' or len(linha)==1:
		return False
	return True
def Linhas(dire):
	return [len([x for x in open(dire+"/"+i).readlines() if olhaLinha(x)]) for i in os.listdir(dire) if verificaNome(i) ]
print sum(Linhas("/home/george/Documentos"))
#08
print "----------------q-08----------------"
def peep(x):
	return(x.next(),range(list(x)[-1]+1) )
k=iter(range(5))
x,a=peep(k)
print x,list(a)
#09
print "----------------q-09----------------"
def my_enumerate(l,x=0):
	if len(l)==1:
		return [(l[0],x)]
	return [(l[0],x)]+my_enumerate(l[1:],x+1)
print my_enumerate(["a","b","c"])
#10
print "----------------q-10----------------"
def zip(l,x):
	if len(x)==1 and len(l)>0:
		return [l[0],x[0]]+l[1:]
	elif len(l)==1 and len(x)>0:
		return [l[0],x[0]]+x[1:]
	else:
		return [l[0],x[0]]+zip(l[1:],x[1:])
print zip([1,2,3,4,5],['a','b','c','d','e','f'])
