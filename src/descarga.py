import os
import time
import threading
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

	def descargar(self):
		self.rango = 2


		