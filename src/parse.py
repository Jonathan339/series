from bs4 import BeautifulSoup
import requests
from config import *



class Conexion(object):

    """Constructor de la clase Conexion"""
    def __init__(self, url):
        self.url = url

    def _conn(self):
        req =  requests.get(self.url)
        soup = BeautifulSoup(req.text, 'lxml')
        return soup

class Jkanime(Conexion):
    """Clase Jkanime que hereda la conexion """

    def __init__(self, url=PAGINA):
        super().__init__(url)
        

    def link(self):
        'Extre el enlace del video que tiene el reproductor'
        self.soup = self._conn()
        src = self.soup.find('iframe', {'class': 'player_conte'})['src'].replace('jk.php?u=','')
        return str(src)
    
    def nombre(self):
        'Obtiene el nombre de la serie'
        nombre = self.soup.find('div', {'class': 'vervideo'})
        return nombre.string
    

    def programacion(self):
        '''
        Extrae la programacion de la pagina y la muestra
        '''
        anime_Name = []
        anime_Url = {}
        items = self.soup.find('ul', {'class': 'ratedul'})
        for item in items:
            name = item.find_all('a')[1].get_text()
            url = item.find_all('a')[1]['href']
            animeNames.append(name)
            animeUrls.update({name: url})

        #return anime_Url, anime_Name
        print(anime_Url)

    def ver_programacion(self):
        'Muestra la programacion'

        conn = Conexion(PAGINA)._conn()
        for item in conn.find_all('ul',{'class':'ratedul'}):
            for litag in item.find_all('li'):
                name = litag.find('a','rated_title').get_text()
                url = litag.find('a','rated_title').get('href')
                cap = litag.find('div',{'class':'rated_stars'}).span.get_text().split()[1]
                dia = litag.find('div',{'class':'rated_stars'}).get_text().split()[2]
                print(MENSAJE_PROGRAMACION.format(name, url, cap, dia))

    def Capitulo(self):
        'Extrae al enlace al capitulo'
        pass

    def ListaCapitulos(self, url):
        'ListaCapitulos que tiene la serie'
        self.url = url
        super().__init__(url)
        for ul_list in self._conn.find_all('ul', {'class':'listpage'}):
            for litag in ul_list.find_all('a'):
                print(litag['href'])
   


class EnlaceReal(Conexion):
    """Esta clase se usa para obtener el enlace real del straming."""

    def __init__(self, url):
        super().__init__(url)

    def enlace(self):
        self.conexion = self._conn
        video = self.conexion.find('video', {'class': 'vjs-tech'})['src']
        print(video)


a = Jkanime('http://jkanime.net/boku-no-kanojo-ga-majimesugiru-sho-bitch-na-ken/2/')
print(a.link())
print(a.nombre())

b = Jkanime().ver_programacion()

#b = Jkanime
#a.ver_programacion()
#b = EnlaceReal(url2)
