
from bs4 import BeautifulSoup
import requests
from PyQt5.QtWebKitWidgets import QWebPage
from PyQt5.QtWidgets import QApplication
import sys

class Conexion(object):

	"""Constructor de la clase Conexion"""
	def __init__(self, url):
		self.url = url

	def _conn(self):
		req =  requests.get(self.url)
		soup = BeautifulSoup(req.text, 'lxml')
		return soup


class Render(QWebPage):
    """Renderiza el HTML con PyQt5 WebKit."""
 
    def __init__(self, html):
        self.html = None
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self._loadFinished)
        self.mainFrame().setHtml(html)
        self.app.exec_()
 
    def _loadFinished(self, result):
        self.html = self.mainFrame().toHtml()
        self.app.quit()




class Enlace(Conexion):
	"""docstring for Enlace"""
	def __init__(self, url):
		super().__init__(url)
		html_video = self._conn()

		#html_render = Render(html_video)

		#titulo = html_video.find('span', {'class' : 'title'}).get_text()
		#vi = html_render.find('video', {'id': 'olvideo_html5_api'})
		print(html_video)


class Link(Render):
	"""docstring for Link"""
	def __init__(self, url):
		
		source_html = requests.get(url).text
		rendered_html = super().__init__(source_html)
		soup = BeautifulSoup(rendered_html, 'lxml')
		video = soup.find('video', {'id': 'olvideo_html5_api'})
		print('url: {0}' .format(rendered_html))




		


url= ('https://openload.co/embed/oB-rkAWAEiE/')

#source = requests.get(url).text
#render = Render(source).html
#_video = BeautifulSoup(render, 'lxml')
#link = _video.find('href')

a = Enlace(url)

#print(link)
		