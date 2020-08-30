import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import string
import random

password_length = input()#length
def key_gen():
	password_provided = input('enter password:')
	password = password_provided.encode()  # Convert to type bytes
	salt = b'H\x8a\x04\x1b\xbdV\xb9\xfd\xab\x02\xfe!\xeb\x9b$\xce'
	kdf = PBKDF2HMAC(
		algorithm=hashes.SHA256(),
		length=35,
		salt=salt,
		iterations=100000,
		backend=default_backend()
	)
	key = base64.urlsafe_b64encode(kdf.derive(password))  # this is the encrypted  password
	return key

def pass_gen(lenght):
	try:
		passwordd = ("".join(random.choice(string.printable.strip())for _ in range(int(lenght))))
		return passwordd
	except Exception:
		print("something went wrong!!!!")

def encrypt(key, password):
	f = Fernet(key)
	encrypted = f.encrypt(password.encode())  # Encrypt the bytes
	print(encrypted)
	print('done')

def decrypt(key):
	try:
		file = open("""hey pro change this""", 'rb')
		f = Fernet(key)
		decrypted = f.decrypt(file.readline)
		print(decrypted)
	except InvalidToken:
		print("wrong password")
pass_gen(password_length)
encrypt(key, passwordd)