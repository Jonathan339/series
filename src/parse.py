from bs4 import BeautifulSoup
import requests


class Conexion(object):

    """Constructor de la clase Conexion"""

    def __init__(self, url):
        self.url = url

    def _conn(self):
        req = requests.get(self.url)
        soup = BeautifulSoup(req.text, 'lxml')
        return soup

class Jkanime(Conexion):
    """Clase Jkanime que hereda la conexion"""

    def __init__(self, url):
        super().__init__(url)
        self.urlbase = 'http://jkanime.net'
        print(self.link())

    def link(self):
        'Extre el enlace del video que tiene el reproductor'
        self.soup = self._conn()
        src = self.soup.find('iframe', {'class': 'player_conte'})[
            'src'].replace('jk.php?u=', '')
        return str(src)

    def nombre(self):
        'Obtiene el nombre de la serie'
        nombre = self.soup.find('div', {'class': 'vervideo'})
        return nombre.string

    '---------------------------------------------'

    def programacion(self):
        '''
        Extrae la programacion de la pagina y la muestra
        '''
        anime_Name = []
        anime_Url = {}
        items = self.soup.find('li', {'class': 'ratedul'})
        for item in items:
            name = item.find_all('a')[1].get_text()
            url = item.find_all('a')[1]['href']
            animeNames.append(name)
            animeUrls.update({name: url})

        return anime_Url, anime_Name
        #print(anime_Url)

    def ver_programacion(self):
        'Muestra la programacion'
        conn = Conexion(self.urlbase)._conn()

        items = conn.find_all('ul', {'class': 'ratedul'})
        #items2 = items.find('li')
        print(items)

        for item in items:
            name = item.find_all('a')[1].get_text()
            print(name)
            url = item.find_all('a')[1]['href']
            #url = item.find('a',{'class':'rated_more'})['href']
            cap = item.span.get_text().split()[1]
            print(
                '''
                    ------------------------------------
                    Nombre:   {0}
                    Enlace:   {1}
                    Capitulo: {2} 
                    ------------------------------------
                '''.format(name, url, cap))

    def Capitulo(self):
        'Extrae al enlace al capitulo'
        pass

    def ListaCapitulos(self):
        'ListaCapitulos que tiene la serie'
        pass
    '--------------------------------------------'


class EnlaceReal(Conexion):
    """docstring for EnlaceReal"""

    def __init__(self, url):
        super().__init__(url)

    def enlace(self):
        self.conexion = self._conn
        #url = self.link()
        video = self.conexion.find('video', {'class': 'vjs-tech'})['src']
        #src =  video.find()
        print('------')
        print(video)


a = Jkanime('http://jkanime.net/boku-no-kanojo-ga-majimesugiru-sho-bitch-na-ken/4/')
#print(a.link())
print(a.nombre())

a.ver_programacion()
#b = EnlaceReal(url2)
