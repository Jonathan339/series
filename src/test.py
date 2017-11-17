import os
from config import PATH_DESCARGA, PATH_ACTUAL

def path(path, file):
		'Cambia de lado la barra lateral según el sistema operativo.'
		if os.name == 'nt':
			path_ruta = path+chr(92)+file
		else:
			path_ruta = path+chr(47)+file
		print(path_ruta)


path(PATH_ACTUAL, 'file.jpg')

print(chr(35))
print(os.name)