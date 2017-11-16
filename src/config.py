import os
#Enlace a la pagina
PAGINA = "http://jkanime.net"

#webdriver Chrome

CHROME = "./bin/chromedriver.exe"

#webdriver
PHANTOMJS_WIN = "phantomjs.exe"


#path donde guarda la descarga.	
PATH_DESCARGA	=	os.path.normpath(os.path.join(os.getcwd(), 'Descargas'))
PATH_ACTUAL = os.path.normpath(os.path.join(os.getcwd()))

print(PATH_ACTUAL)

EXTENCION	= ".mp4"
#Mensaje que se muestra al iniciar la descarga del archivo.
#recibe como parametro:
#Nombre, Tamaño, Velocidad, Tiempo restante
MENSAJE_DESCARGA 	= 	"""Descargando: {0}
						   Tamaño:      {1}
						   Velocidad:   {2}
						   T. Restante: {3}
		               	 """

MENSAJE_PROGRAMACION	=  '''
                    ------------------------------------
                    Nombre:   {0}
                    Enlace:   {1}
                    Capitulo: {2} 
                    Dia:      {3}
                    ------------------------------------
                '''

					    
#Mensaje por problemas en la conexion con la pagina
MENSAJE_ERROR_PAGINA	= "No se pudo cargar la pagina web"


DIGITOS_MAXIMOS	= 3

PAGINA_INICIAL = 1
