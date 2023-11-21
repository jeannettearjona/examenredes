import os

def encrypt_image(file_path, encryption_key):
    try:
        # Open the file for reading
        with open(file_path, 'rb') as fin:
            # Read the image data
            image_data = fin.read()

        # Convert the image data into a bytearray
        image = bytearray(image_data)

        # Perform XOR operation on each value of the bytearray with the key
        for index, value in enumerate(image):
            image[index] = value ^ encryption_key

        # Get the file extension from the original file path
        _, file_extension = os.path.splitext(file_path)

        # Construct a new file path with '_encrypted' appended to the original file name
        encrypted_file_path = file_path.replace(file_extension, f'_encrypted{file_extension}')

        # Open the new file for writing
        with open(encrypted_file_path, 'wb') as fout:
            # Write the encrypted data to the new file
            fout.write(image)

        print('Encryption Done. Encrypted file saved at:', encrypted_file_path)

    except Exception as e:
        print('Error caught:', e)

# take path of image as input
path = input(r'Enter path of Image: ')

# taking encryption key as input
key = input('Enter Key for encryption of Image: ')

try:
    # Convert the key to an integer
    key = int(key)

    # Check if the file at the specified path exists
    if os.path.exists(path):
        encrypt_image(path, key)
    else:
        print('Error: File not found at the specified path.')

except ValueError:
    print('Error: Please enter a valid integer key.')
except Exception as e:
    print('Error caught:', e)
