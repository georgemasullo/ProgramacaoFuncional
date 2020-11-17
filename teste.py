def inserir(x,esq=None,dire=None):
	return(x,esq,dire)
def lista(xs):
	if xs is None:
		return None
	return (xs[0],lista(xs[1]),lista(xs[2]))
def con(raiz,valor):
	if raiz is None:
		return inserir(valor)
	elif valor<raiz[0]:
		return re_equilibrar((raiz[0],con(raiz[1],valor),raiz[2]))
	elif valor>raiz[0]:
		return re_equilibrar((raiz[0],raiz[1],con(raiz[2],valor)))
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
def altura(no):
	def max(esq,dire):
		if esq>dire:
			return esq
		return dire
	if no is None:
		return 0
	return 1+max(altura(no[1]),altura(no[2]))
def desvio(no):
	if no is None:
		return 0
	return altura(no[1])-altura(no[2])
def corrige_dir (arv):
	if desvio(arv[1])==-1:
		return rotacaoDE(arv)
	return rotacaoE(arv)
def corrige_esq(arv):
	if desvio(arv[2])==1:
		return rotacaoED(arv)
	return rotacaoE(arv)
def re_equilibrar(arv):
	if desvio(arv)==2:
		return corrige_dir(arv)
	if desvio(arv)==-2:
		return corrige_esq(arv)
	return arv
def rotacaoD(arv):
	return (arv[1][0],arv[1][1],inserir(arv[0],None,arv[2]))
def rotacaoE(arv):
	return(arv[2][0],inserir(arv[0],None,arv[1]),arv[2][2])
def rotacaoED(arv):
	def rt(no):
		return (no[0],rotacaoE(no[1]),no[2])
	return rotacaoD(rt(arv))
def rotacaoDE(arv):
	def rt(no):
		return (no[0],no[1],rotacaoD(no[2]))
	return rotacaoE(rt(arv))
a=con(None,2)
a=con(a,4)
print a
a=con(a,5)
print a
a=con(a,7)
print a
a=con(a,8)
print a
a=con(a,9)
print a
a=con(a,11)
print a
a=con(a,15)
print a
a=con(a,1)
print a
