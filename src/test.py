import platform
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException


class Cliente_Chrome(object):

    def __init__(self, url):
        self.url = url
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        #self.browser = webdriver.Chrome()
        self.start = time.time()
        self.browser.get(self.url)
        #self.browser.save_screenshot('screen.png')
        overlay_splash = self.browser.find_element_by_id('videooverlay')
        overlay_splash.click()
        #button = self.browser.find_element_by_class_name('vjs-big-play-button')
        #button.click()

    def url_video(self):
        pagina = BeautifulSoup(self.browser.page_source, 'lxml')
        url_video = pagina.find('video', {'id': 'olvideo_html5_api'})['src']
        url = 'https://openload.co'+url_video
        print('https://openload.co' + url_video)
        fin = time.time() - self.start
        print('Segundos: %.3f' % fin)
        self.browser.quit()
        #return url


class Cliente_Phantomjs(object):

	def __init__(self, url):
		self.url = url
		self.browser = webdriver.Chrome()
		#self.browser = webdriver.PhantomJS()
		#self.browser.set_window_size(1000, 700)
		self.start = time.time()
		self.browser.get(self.url)
		self.browser.save_screenshot('screen.png')
		# selecciona el elemento al que se hace click
		overlay_splash = self.browser.find_element_by_id('videooverlay')
		overlay_splash.click()
		#button = self.browser.find_element_by_id('anim-container')
		#button.click()
		


	def url_video(self):
		pagina = BeautifulSoup(self.browser.page_source, 'lxml', from_encoding="utf-8")
		pagina1 = self.browser.page_source
		print(pagina1)
		print('-'*100)
		url_video = pagina.find('video', {'id': 'olvideo_html5_api'})['src']
	    # url = 'https://openload.co'+url_video
		print('https://openload.co' + str(url_video))
		fin = time.time() - self.start
		print('phantomjs')
		print('Segundos: %.3f' % fin)
		self.browser.quit()

	def sistema(self):
		if platform.system() == 'Windows':
			PHANTOMJS_PATH = './bin/phantomjs.exe'
		else:
			PHANTOMJS_PATH = './bin/phantomjs'
		return PHANTOMJS_PATH



url = ('https://openload.co/embed/oB-rkAWAEiE/')
a = Cliente_Chrome(url).url_video()

#a.url_video()

#b = Cliente_Phantomjs(url).url_video()
