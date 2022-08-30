from cryptography.fernet import fernet 

texto="x?1_P-1M.4!eM"
key = fernet.generate_key()
objeto_cifrado= fernet(key)
texto_encriptado = objeto_cifrado.encrypt(str.encode(texto))
print(texto_encriptado)