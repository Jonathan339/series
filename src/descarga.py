import os, shutil, sys
import time, decimal
import requests
from pathlib import Path
from config import *

class Descarga:
	"""docstring for Descarga"""
	def __init__(self, url, nombre):
		
		"""La clase recibe como parametros las conexiones, el tamaño o rango y la url."""
		
		self.url = url
		self.nombre = nombre + EXTENCION
		#obtiene el tañano del archivo
		self.file_size = requests.get(self.url, stream=True).headers['Content-length']

		self.directorio()
		self.size()


	def size(self):
		"""Este metodo devuelve el tamaño real del archivo."""
		sf = self.file_size
		kb = 2**10
		mb = 2**20
		gb = 2**30
		tb = 2**40
		if int(sf) >= kb and int(sf) <= mb:
			size_file = round(int(sf)/kb, 1)
		elif int(sf) >= mb and int(sf) <= gb:
			size_file = round(int(sf)/mb, 1)
		elif int(sf) >= gb and int(sf) <= tb:
			size_file = round(int(sf)/gb, 1)
		return size_file


	def descargar(self):
		"""Metodo que realiza la descarga. Retorna el archivo en el directorio indicado
		   en el modulo config.py en la variable PATH_DESCARGA.
		"""
		
		#obtiene la respuesta del servidor para descargar
		r = requests.get(self.url, stream=True)
		with open(self.nombre, 'wb') as f:
			for chunk in r.iter_content(chunk_size=1024):
				if chunk: # filtrar las nuevas parter del archivo 
					f.write(chunk)
		return self.move(self.nombre)


	def directorio(self, file=None):
		"""Crea la carpeta Descargas si no existe."""
		if not os.path.exists(PATH_DESCARGA):
			path = os.mkdir(PATH_DESCARGA)
		else:
			path = PATH_DESCARGA
		return path

	def path(self, path, file):
		"""Cambia de lado la barra lateral según el sistema operativo."""
		if os.name == 'nt':
			path_archivo = path+chr(92)+file
		else:
			path_archivo = path+chr(47)+file
		return path_archivo

	def move(self, file):
		"""mueve el archivo a la carpeta Directorio. Si el archivo ya existe se sobreescribe."""
		
		if os.path.isdir(PATH_DESCARGA):
			if os.path.exists(file):
				shutil.move(os.path.join(self.path(PATH_ACTUAL, file)), os.path.join(self.path(PATH_DESCARGA, file)))
			else:
				print('El archivo no existe.')
		else:
			print('El directorio no existe.')
		

	


url = 'http://cdn.jkanime.net/assets/images/logo.png'
a = Descarga(url,'k.png').descargar()