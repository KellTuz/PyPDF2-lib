from PyPDF2 import PdfWriter, PdfReader
import sys


# File encryption
def encrypt_file():
	file_path = input('[+] Enter file path: ')
	password = input('[+] Enter password: ')
	encrypted_file_name = input('[+] Enter a name for the encrypted file: ')

	try:
		file_reader = PdfReader(file_path)
	except FileNotFoundError:
		print(f'[INFO] No file with path: {file_path}')
		sys.exit()

	file_writer = PdfWriter()

	for page in range(len(file_reader.pages)):
		file_writer.add_page(file_reader.pages[page])

	file_writer.encrypt(password)

	with open(encrypted_file_name, 'wb') as file:
		file_writer.write(file)

	print(f'[+] Created - {encrypted_file_name}')


# File decryption
def decrypt_file():
	file_path = input('[+] Enter file path: ')
	password = input('[+] Enter password: ')
	decrypted_file_name = input('[+] Enter a name for the decrypted file: ')

	try:
		file_reader = PdfReader(file_path)
	except FileNotFoundError:
		print(f'[INFO] No file with path: {file_path}')
		sys.exit()

	if file_reader.is_encrypted:
		file_reader.decrypt(password)

	file_writer = PdfWriter()

	for page in range(len(file_reader.pages)):
		file_writer.add_page(file_reader.pages[page])

	with open(decrypted_file_name, 'wb') as file:
		file_writer.write(file)

	print(f'[+] Created - {decrypted_file_name}')


def main():
	choose = input('[+] Enter 0 to encrypt the file, enter 1 to decrypt: ')
	encrypt_file() if choose == '0' else decrypt_file()


if __name__ == '__main__':
	main()
