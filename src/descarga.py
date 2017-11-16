import os, shutil, sys
import time
import requests
from pathlib import Path
from config import *

class Descarga:
	"""docstring for Descarga"""
	def __init__(self, url, nombre):
		'''
		La clase recibe como parametros las conexiones, el tamaño o rango y la url.
		'''
		self.path = os.path.join(PATH_DESCARGA + chr(92)+nombre)
		#self.conexiones = conexiones
		self.url = url
		self.nombre = nombre #+ EXTENCION
		self.directorio()


	def descargar(self):
		# NOTE the stream=True parameter
		r = requests.get(self.url, stream=True)
		with open(self.nombre, 'wb') as f:
			for chunk in r.iter_content(chunk_size=1024):
				if chunk: # filter out keep-alive new chunks
					f.write(chunk)
		return self.move(self.nombre)


	def directorio(self, file=None):
		'''Crea la carpeta Descargas si no existe.'''
		if not os.path.exists(PATH_DESCARGA):
			path = os.mkdir(PATH_DESCARGA)
		else:
			path = PATH_DESCARGA
		return path

	def path(self, _path, file):
		'Cambia de lado la barra lateral según el sistema operativo.'
		if os.name == 'nt':
			_path = _path+chr(92)+file
		else:
			_path = _path+chr(47)+file
		return path

	def move(self, file):
		'''mueve el archivo a la carpeta Directorio. Si el archivo ya existe se sobreescribe.'''
		#path_actual = os.path.normpath(os.path.join(os.getcwd()+chr(92)+file))
		#path_actual = self.path(PATH_ACTUAL, file)
		#path_carpeta = PATH_DESCARGA + chr(92)+file
		#path_carpeta = self.path(PATH_DESCARGA, file)
		if os.path.exists(file):
			shutil.move(os.path.join(self.path(PATH_ACTUAL, file)), os.path.join(self.path(PATH_DESCARGA, file)))
		else:
			print('El archivo no existe.')
		
		

	


url = 'http://cdn.jkanime.net/assets/images/logo.png'
a = Descarga(url, 'k.png').descargar()