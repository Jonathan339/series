import platform
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options


class Cliente(object):

    """Constructor de la clase Conexion"""

    def __init__(self, url):
        self.url = url
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        self.start = time.time()
        req = self.browser.get(self.url)
        cliente = Cliente(self.url)
        cliente.overlay_splash()
        cliente.button()
        print(url_video())

    def ovelay_splash(self):
        overlay_splash = self.browser.find_element_by_id('videooverlay')
        overlay_splash.click()

    def button(self):
        button = self.browser.find_element_by_class_name('vjs-big-play-button')
        button.click()

    def url_video(self):
        pagina = BeautifulSoup(self.browser.page_source, 'lxml')
        url_video = pagina.find('video', {'id': 'olvideo_html5_api'})['src']
        #url = 'https://openload.co'+url_video
        print('https://openload.co' + url_video)
        fin = time.time() - self.start
        print('Segundos: %.3f' % fin)
        self.browser.close()
        # return url

    def Sistema(self):

        if platform.system() == 'Windows':
            PHANTOMJS_PATH = './bin/phantomjs.exe'
        else:
            PHANTOMJS_PATH = './bin/phantomjs'
        return PHANTOMJS_PATH


url = ('https://openload.co/embed/oB-rkAWAEiE/')
a = Cliente(url)
# a.url_video()
