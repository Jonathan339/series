import sys
from descarga import Descarga
from parse import Parse, Conexion


		

class Menu(descarga):
	"""docstring for Menu"""
	def __init__(self):
		super(descarga, self).__init__()
		opciones = { 1 : self.descarga,
		             2 : self.descarga_masiva,
		             3 : self.salir}
	def Menu(self):
		print("""
    		   1 - Descargar capitulo
    		   2 - Descarga masiva
    		   3 - Buscar
    		   4 - Salir
    		""")
	
	def descarga_cap(self):
		#print("""Ingrese la url del capitulo""")
		url = input("Ingrese la url del capitulo")

		
	
	def help(self):
		pass
    	


		

a = Menu()
input()
		