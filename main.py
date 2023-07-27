from cryptography.fernet import Fernet
key = Fernet.generate_key()
crypter = Fernet(key)
string=crypter.encrypt(b'heypulse')
decrypt = crypter.decrypt(string)
print(str(string,'utf8'))
print(str(decrypt,'utf8'))