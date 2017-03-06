


class Nodo:
	def __init__(self, numero=None, palabra=None, siguiente=None):
	     self.numero = numero
	     self.palabra = palabra
	     self.siguiente = siguiente

	def __str__(self):
	     return "%s" %(self.palabra)

class lSimples:
	def __init__(self):
	 self.cabeza = None
	 self.cola = None

	def agregar (self, elemento):
	 if self.cabeza == None:
	 	self.cabeza = elemento

	 if self.cola !=None:
	 	self.cola.siguiente = elemento

	 self.cola = elemento

	def agregarenf (self, elemento):
	 if self.cabeza == None:
	 	self.cabeza = elemento

	 if self.cola !=None:
	  elemento.siguiente = self.cabeza

	 self.cola = self.cabeza
	 self.cabeza = elemento






	def listar (self):
	 	aux = self.cabeza
	 	while aux != None:
	 		print(aux)
	 		aux = aux.siguiente



	def buscar (self, palabra):
	 	aux = self.cabeza
	 	while aux != None:
	 		if aux.palabra == palabra:
	 			return aux
	 		aux = aux.siguiente
	 	return None   

	def eliminar (self, palabra):
	 	if self.cabeza.palabra == palabra:
	 	  self.cabeza = cabeza.siguiente
	 	  return True
	 	else:
	 		aux = self.cabeza
	 		anterior = aux
	 		while aux != None:
	 			if aux.palabra == palabra:
	 				anterior.siguiente = aux.siguiente
	 				return True
	 			anterior = aux
	 			aux = aux.siguiente
	 	return False
	

	def printer (self):
	 	path = 'C:\\Users\\dell\\Documents\\Usac\\Semestre 9\\Estructuras de datos\\practica2\\testtext.txt'
	 	file = open(path,"w") 
	 	file.write("Hello\n")
	 	file.write("Im") 
	 	file.write("fucking") 
	 	file.write("tired")
	 	file.close() 


    		


if __name__ == "__main__":
	ls = lSimples()

	while(True):
		print("---Menu---\n" + 
			"1. Agregar\n" + 
			"2. Listar\n" + 
		    "3. Buscar\n"+
		    "4. Eliminar\n")
		num = input("ingrese la opcion")
		if num == "1":
			palabra= input("ingrese la palabra: ")
			nod= Nodo( 1,palabra)
			ls.agregar(nod)
		elif num == "2":
			ls.listar()
		elif num == "3":
			palabra = input ("Ingrese la palabra: ")
			result = ls.buscar(palabra)
			if result is not None:
				print (result)
			else:
				print("Registro no encontrado")
		elif num == "4":
			palabra = input ("Ingrese la palabra: ")
			if(ls.eliminar(palabra)):
				print ("Registro borrado con exito")
			else:
				print ("Se encontraron errores al pr ocesar")
		elif num == "5":
			palabra= input("ingrese la palabra: ")
			nod= Nodo( 1,palabra)
			ls.agregarenf(nod)
		elif num == "6":
			ls.printer()
