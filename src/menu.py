import sys

from config import *
from descarga import Descarga
from parse import Conexion,Jkanime 


		

class Menu():
	"""docstring for Menu"""
	def __init__(self):
		self.descarga = Descarga()
		self.jkanime = Jkanime()
		elecciones = { 1 : self.descarga,
		             2 : self.descarga_masiva,
		             3 : self.salir}
		
	def run(self):
		while True:
			self.mostrar_menu()
			eleccion = input("Seleccione una opcion: ")
			accion = self.elecciones.get(eleccion)
			if accion:
				accion()
			else:
				print('{0} no es una opcion valida.'.format(eleccion))
				
		
	def mostrar_menu(self):
		print("""
    		   1 - Descargar capitulo
    		   2 - Descarga masiva
    		   3 - Salir
    		""")
	
	def descarga_cap(self):
		#print("""Ingrese la url del capitulo""")
		url = input("Ingrese la url del capitulo")
		link = self.jkanime(url).link()
		self.descarga(link)

		
	
	def help(self):
		pass
    	

