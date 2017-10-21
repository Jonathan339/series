import os
import time
from multiprocessing import Process, Manager
import requests

class Descarga(object):
	"""docstring for Descarga"""
	def __init__(self, conexiones, rango, url):
		'''
		La clase recibe como parametros las conexiones, el tamaño o rango y la url.

		'''
		self.conexiones = conexiones
		self.url = url
		self.rango = rango

	def descarga(self):
		try:
			HeaderRange = {'Range': 'bytes={}-{}'.format(*rango)}
			req = requests.get(self.url, header=HeaderRange)
			
			
		except Exception as e:
			raise e
		else:
			pass

	def descarga_paralela(self):
		pass
		