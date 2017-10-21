import sys
from src.parse import *
from src.menu import *

def main():
	pass

if __name__ == '__main__':

	conn = sys.argv[1]
	url = sys.argv[2]
	if conn != None:
		if conn == '8' or conn == '16' or conn == '32':
		    conn = conn
		else:
			print('no se aceptan otras conexiones fuera de 8, 16 o 32')

			if conn == None:
				url = conn
				Menu = menu()
				Menu.Menu()
				parse = Jkanime(url)





	

	main()
