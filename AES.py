pip install pycryptodome

from Crypto.Cipher import AES
from Crypto.Hash import SHA256

#Accept input string from user
password = input("Please enter your password: ")
print(password)

#Encode password to bytes from string then hash
hash = SHA256.new(password.encode('utf-8'))

#Convert to length 32byte and pass value to key variable
key = hash.digest()
print(key)
len(key)

#AES encryption function
def aes_encrypt(data):
    msg = data
    block_size = 16
    pad = "["
    padding = lambda m: m + (block_size - len(m) % block_size) * pad
    cipher = AES.new(key, AES.MODE_ECB)
    result =cipher.encrypt(padding(msg).encode('utf-8'))
    return result

#Input message to be encrypted
msg = input("Write your message: ")

#Pass msg into encryption function and save to cypher text variable
cypher_text = aes_encrypt(msg)

#print the cypher text
print(cypher_text)

#Decryption function
def decrypt(data):
    msg = data
    pad = "["
    decipher = AES.new(key, AES.MODE_ECB)
    paded_plain_text = decipher.decrypt(msg).decode('utf-8')
    index = paded_plain_text.find(pad)
    result = paded_plain_text[:index]
    return result

#Pass cypher_text into decryption function and save to plain text variable
plain_text = decrypt(cypher_text)

#print plain text
print(plain_text)