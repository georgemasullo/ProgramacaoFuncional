from math import sqrt
class Vetor3D:
	def __init__(self,x,y,z):
		self.__x=x
		self.__y=y
		self.__z=z
	def get__x(self):
		return self.__x
	def get__y(self):
		return self.__y
	def get__z(self):
		return self.__z
	#x=property(get__x)
	def soma(self,v):
		x=Vetor3D(self.__x+v.get__x,self.__y+v.get__y,self.__z+v.get__z)
		return x
	def inverso(self):
		v=Vetor3D(self.__x*(-1),self.__y*(-1),self.__z*(-1))
		return v
	def prod_por_escalar(self,x):
		v=Vetor3D(self.__x*x,self.__y*x,self.__z*x)
		return v
	def modulo(self):
		return sqrt(self.__x**2+self.__y**2+self.__z**2)
	def unitario(self):
		modulo=self.modulo()
		v=Vetor3D(self.__x/modulo,self.__y/modulo,self.__z/modulo)
		return v
	def igualdade(self,v):
		if v.get__x==self.__x and v.get__y==self.__y and v.get__z==self.__z:
			return True
		return False
if __name__=="__main__":
	v=Vetor3D(3,2,3)
	print (v.x)
	print (v.get__y())
	print (v.get__z())

	x=v.prod_por_escalar(2)
	print (x.get__x())
	print (x.get__y())
	print (x.get__z())
