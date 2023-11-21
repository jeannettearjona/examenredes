# try block to handle the exception
try:
	#toma la ruta de imagen encriptada
	path = input(r'Enter path of Image : ')
	
	#toma la llave para decencriptar
	key = int(input('Enter Key for encryption of Image : '))
	
	#imprime
	print('The path of file : ', path)
	print('Note : Encryption key and Decryption key must be same.')
	print('Key for Decryption : ', key)
	
	#abre archivo para lectura
	fin = open(path, 'rb')
	
	#almacena datos de la imagen
	image = fin.read()
	fin.close()
	
	#convierte la imagen en un bytearray para realizar la desencriptación
	image = bytearray(image)

	#realiza la operación XOR en cada valor del bytearray
	for index, values in enumerate(image):
		image[index] = values ^ key

	#abre archivo de escritura
	fin = open(path, 'wb')
	
	#escribe los datos de desencriptación en la imagen
	fin.write(image)
	fin.close()
	print('Decryption Done...')

#manejo de cualquier error
except Exception:
	print('Error caught : ', Exception.__name__)
