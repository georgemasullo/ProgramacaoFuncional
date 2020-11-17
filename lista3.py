#01
print "q-01"
def somatorio(numeros):
	if len(numeros)==0:
		return 0
	return numeros[0]+somatorio(numeros[1:])
def filtra(ini,lista,filtro):
	if ini== len(lista):
		return []
	if filtro(lista[ini]):
		return [lista[ini]] + filtra(ini+1,lista,filtro)
	else:
		return filtra(ini+1,lista,filtro)
l=[1,2,3,4]
n=2
#a
print "a"
print somatorio(filtra(0,l,lambda v:v%n==0))
#b
print "b"
print somatorio(filtra(0,l,lambda v:n%v==0))
#c
print "c"
print somatorio(filtra(0,l,lambda v:v>n))
#02
def coefiente_Binimial(n,k):
	def fatorial(n): 
   		if n<=1: 
      			return 1
   		else: 
	 		return n*fatorial(n-1)
	return fatorial(n)/(fatorial(k)*fatorial(n-k))
print "q-02"
print coefiente_Binimial(4,3) 
#03
print "q-03"
def triangulo_pascal(ini,n):
	def repeticao(ini,n,num):
		if ini==n:
			return [(num,ini)]
		return [(num,ini)] +repeticao(ini+1,n,num)
	if ini==n:
		return [(repeticao(0,n,ini))]
	return [(repeticao(0,ini,ini))]+triangulo_pascal(ini+1,n)

print triangulo_pascal(0,2)
#04
print "q-04"

