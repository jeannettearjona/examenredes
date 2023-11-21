import os

def encrypt_image(file_path, encryption_key):
    try:
        #abre archivo de lectura
        with open(file_path, 'rb') as fin:
            #lectura de datos de img
            image_data = fin.read()

        #convierte datos de imagen en un bytearray
        image = bytearray(image_data)

        #realiza la operación XOR en cada valor del bytearray con la clave
        for index, value in enumerate(image):
            image[index] = value ^ encryption_key

        #obtiene la extensión del archivo desde el path original del archivo
        _, file_extension = os.path.splitext(file_path)

        #construye un nuevo path de archivo con '_encrypted' añadido al nombre original del archivo donde guarda la img encriptada por si cualquier cosa
        encrypted_file_path = file_path.replace(file_extension, f'_encrypted{file_extension}')

        #abre el nuevo archivo para escritura
        with open(encrypted_file_path, 'wb') as fout:
            #escribe los datos encriptados al nuevo archivo
            fout.write(image)

        print('Encryption Done. Encrypted file saved at:', encrypted_file_path)

    #maneja cualquier excepción que pueda ocurrir durante el proceso de encriptación
    except Exception as e:
        print('Error caught:', e)

#toma el path de la imagen como entrada
path = input(r'Enter path of Image: ')

#toma la clave de encriptación como entrada
key = input('Enter Key for encryption of Image: ')

try:
    #convierte clave en entero
    key = int(key)

    #checa si existe el path
    if os.path.exists(path):
        encrypt_image(path, key)
    else:
        print('Error: File not found at the specified path.')

except ValueError:
    #error de si clave no es un int
    print('Error: Please enter a valid integer key.')
except Exception as e:
    #cualquier otro error
    print('Error caught:', e)
