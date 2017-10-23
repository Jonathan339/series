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

	def descarga(self, url,orden,rango,frag):
		try:
			Header = {'Range': 'bytes={}-{}'.format(*rango),
			              'User-Agent':'Mozilla/5.0'}
			req = requests.get(self.url, header=Header)
			data = requests.post(self.url, files=req)
			if data:
				frag[data]=data
				print('Fragmento {} descargado correctamente. Obtenidos {} bytes.'.format(orden,len(data)))
			else:
				frag[orden]=None
			except:
				frag[orden]='#Error'
				raise
		

	def descarga_paralela(self, url, fragmentos, nombre):
		with requests.get(url, stream=True) as reqs:
			reqs.raise_for_status()
			with open('Forest.mp4', 'wb') as fd:
				for chunk in req.iter_content(chunk_size=512):
					print('Received a Chunk')
					fd.write(chunk)
		