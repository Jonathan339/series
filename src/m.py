import platform
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options 


# Diferentes PhantomJS para distintos Sitemas Operativos
# Windows 32 y 64 bit y linux 
if platform.system() == 'Windows':
    PHANTOMJS_PATH = './bin/phantomjs.exe'
else:
    PHANTOMJS_PATH = './bin/phantomjs'

#uso PhantomJS como webbrowser para cargar la pagina
browser = webdriver.PhantomJS(PHANTOMJS_PATH)
#chrome_options = Options()  
#chrome_options.add_argument("--headless")
#browser = webdriver.Chrome(chrome_options=chrome_options)

url= ('https://openload.co/embed/HlZrvLnhjWk/')
start = time.time()
r = browser.get(url)
#selecciona el elemento al que se hace click
#<div id="videooverlay" style="display: none;"></div>
overlay_splash = browser.find_element_by_id('videooverlay')
overlay_splash.click()
'''<button class="vjs-big-play-button" type="button" aria-live="polite" title="Play Video" aria-disabled="false">
<span class="vjs-control-text">Play Video</span>
</button>'''

button = browser.find_element_by_class_name('vjs-big-play-button')
#button = browser.find_element_by_css_selector('button.vjs-big-play-button')
#button = browser.find_element_by_xpath('//*[@id="olvideo"]/button')
button.click()

#obtengo la pagina
pagina   = BeautifulSoup(browser.page_source, 'lxml')
#enlace descargable del video
url_video = pagina.find('video', {'id': 'olvideo_html5_api'})['src']
print('https://openload.co'+url_video)
fin = time.time() - start
print('Segundos: %.3f'% fin)
browser.close()
#dlbutton0