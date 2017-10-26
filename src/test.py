
from bs4 import BeautifulSoup
import requests


class Conexion(object):

	"""Constructor de la clase Conexion"""
	def __init__(self, url):
		self.url = url

	def _conn(self):
		req =  requests.get(self.url)
		soup = BeautifulSoup(req.text, 'lxml')
		return soup

class Enlace(Conexion):
	"""docstring for Enlace"""
	def __init__(self, url):
		super().__init__(url)
		video = self._conn()
		src = video.find_all('src')
		print(video)


a = Enlace('https://openload.co/embed/oB-rkAWAEiE/')
		