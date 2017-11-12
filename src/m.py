import sys
import requests
from bs4 import BeautifulSoup
from PyQt5.QtWebKitWidgets import QWebPage
from PyQt5.QtWidgets import QApplication


class Render(QWebPage):
    """Render HTML with PyQt5 WebKit."""

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


class Sesion():
	def __init__(self, url):
		source_html = requests.get(url).text
		self.render = Render(source_html).html
		soup = BeautifulSoup(self.render, 'html.parser')

	def render(self):
		print(self.render)



url = 'https://openload.co/embed/oB-rkAWAEiE/'
a = Sesion(url)
a.render()

# get the raw HTML
#source_html = requests.get(url).text

# return the JavaScript rendered HTML
#with Display(visible=0, size=(800, 600)):
#rendered_html = Render(source_html).html

# get the BeautifulSoup
#soup = BeautifulSoup(rendered_html, 'html.parser')

#print(rendered_html)

