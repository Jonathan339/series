try:
	from bs4 import BeautifulSoup
	import request
except ImportError as e:
	raise ("Faltan instalar librerias: \n {0}".format(e) )
else:
	pass


class ListaCapitulos(list):
	lista = []
	"""Clase donde se listan todos los capitulos"""
	def __init__(self, arg):
		super().__init__()
		self.arg = arg 

class Lista(dict):
	"""Clase donde se agrupa la lista de capitulos 
	   con su correspondiente numero de capitulo."""
	def function(self):
		pass
		
		


class Conexion(object):

	"""Constructor de la clase Conexion"""
	def __init__(self, url):
		self.url = url

	def _conn(self):
		req =  requests.get(self.url)
		soup = BeautifulSoup(resp.text, 'lxml')
		return soup

class Jkanime(Conexion):
	"""Clase Jkanime que hereda la conexion"""

	def __init__(self, url):
		super().__init__(url)
		self.urlbase = 'http://jkanime.net'


     #-------------
     def link(self):
     	#req = requests.get(self.url)
        #self.soup = bs(req.text, "html.Parser")
        self.soup = _conn()
        src = self.soup.find('iframe', {'class': 'player_conte'})[
            'src'].replace('jk.php?u=', '')
        return str(src)

    def nombre(self):
        nombre = self.soup.find('div', {'class': 'vervideo'})
        return nombre.string

    def programacion(self):

        items = self.soup.find('li', {'class': 'ratedul'})
        anime_Name = []
        anime_Url = {}
        for item in items:
            name = item.find_all('a')[1].get_text()
            url = item.find_all('a')[1]['href']
            animeNames.append(name)
            animeUrls.update({name: url})
        return anime_Url, anime_Name
        print(anime_Url)

    def ver_programacion(self):

    	for item in items:
    		items = self.soup.find('ul', {'class': 'ratedul'})
    		name2 = items.find_all('a').get_text()
    		print(name2)

	def Capitulo(self):
		pass

a = Jkanime()
print(a.ver_programacion())







		
		
		