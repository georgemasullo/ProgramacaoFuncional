from itertools import *
import operator
from itertools import islice
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
def aux(i,ma,f,x=0):
	if len(i)-1==x:
		return [ i[x] +[f for k in range(ma - len(i[x]))] ]
	return [i[x] +[f for k in range(ma - len(i[x]) )]] + aux(i,ma,f,x+1)
print aux(l,len(l[maxi(l)]),'-')
def iterc(l,tam):
	return [[ i[x] for i in [k for k in l] ] for x in range(tam)]
print iterc(aux(l,len(l[maxi(l)]),'-'),len(l[maxi(l)]))
def uni(l):
	if len(l)==1:
		return str(l[0])
	return str(l[0])+uni(l[1:])
print uni(iterc(aux(l,len(l[maxi(l)]),'-'),len(l[maxi(l)]))[0])
