import os
import time
import threading
from multiprocessing import Process, Manager
import requests
from config import *

class Descarga(object):
	"""docstring for Descarga"""
	def __init__(self, conexiones, directorio, url, nombre):
		'''
		La clase recibe como parametros las conexiones, el tamaño o rango y la url.
		'''
		self.conexiones = conexiones
		self.url = url
		self.nombre = nombre

	def descargar(self):
		# NOTE the stream=True parameter
		r = requests.get(self.url, stream=True)
		with open(self.nombre, 'wb') as f:
			for chunk in r.iter_content(chunk_size=1024):
			if chunk: # filter out keep-alive new chunks
			f.write(chunk)
		return self.nombre+EXTENCION

	def partes(self):
		return partes_tamaño


		