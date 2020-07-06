from math import pow
import os
import random
import base64
import sys, socket, select
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA


os.system('mode con: cols=49')

encrypt_char_list = []

def encrypt_message(msg, e, n):
    BLOCK_SIZE = 32
	PADDING = '{'
	pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
	EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
	cipher = AES.new(public_key)
	encrypted_message = EncodeAES(public_key, msg)
    conn.send(encrypted_message.encode())
    return encrypted_message

def decrypt_message(msg, d, n):
	BLOCK_SIZE = 32
	PADDING = '{'
	pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
	DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
	cipher = AES.new(private_key)
	decrypted_message = DecodeAES(private_key, msg)
	return decrypted_message    

def generate_key(p, q):
    n = p * q
    e = 2
    phi = (p - 1) * (q - 1)

    while(True):
        if(gcd(e, phi) == 1):
            break
        else:
            e = e + 1
    k = 2
    d = (1 + (k * phi)) / e

    if(d != int(d)):
        while(True):
            print('ERROR: d must be intiger.')
    d = int(d)
    return e, d, n

def send_public_key(e, n):
    public_key = ''
    exponent = str(e)
    modulus = str(n)
   
    while(len(exponent) != 5):
        exponent = '0' + exponent
    while(len(modulus) != 5):
        modulus = '0' + modulus

    public_key = exponent + modulus
    client.send(public_key.encode())

def recieve_public_key():
    key = ''
    public_key = []
    recieved_data = client.recv(4096).decode()

    for data in recieved_data:
        key = key + data
        if(len(key) == 5):
            public_key.append(int(key))
            key = ''
    return public_key[0], public_key[1]

def RSAencrypt(symmetric, public_exp, public_mod):
    encrypted_symmetric = ""
    for i in range(0, len(symmetric)):
        encrypted_symmetric += str(RSA.endecrypt(ord(symmetric[i]), public_exp, public_mod)) + ","
    return encrypted_symmetric



print('=================================================')
print('     COMPUTER NETWORKS-2 FINAL HW (ALICE)        ')
print('=================================================')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

IP_Address = '127.0.0.1'
print('IP Address: 127.0.0.1')
Port = 8888
print('Port      : 8888')
print('=================================================')

client.connect((IP_Address, Port))

symmetric_key = random.randint(1, 10)
client_e, client_d, client_n = generate_key(23, 17)
send_public_key(client_e, client_n)
server_e, server_n = recieve_public_key()
encrypted_symmetric_key = RSAencrypt(symmetric_key, server_e, server_n)
client.send(encrypted_symmetric_key.encode())


print('Symmetric Key                 = ' + str(symmetric_key))
print('=================================================')
print('Client Public Key (Exponent)  = ' + str(client_e))
print('Client Public Key (Modulus)   = ' + str(client_n))
print('Client Private Key (Exponent) = ' + str(client_d))
print('Client Private Key (Modulus)  = ' + str(client_n))
print('=================================================')
print('Server Public Key (Exponent)  = ' + str(server_e))
print('Server Public Key (Modulus)   = ' + str(server_n))
print('=================================================')


while(True):
    send_message = ''
    print('\n=================================================')
    send_message = input('Message: ')
    print('=================================================')
    print('Sended data = ' + encrypt_message(send_message, client_e, client_n)
    print('=================================================')
    print('Wait...')
    print('=================================================')
    receive_message = conn.recv(4096).decode()
    print('Recieved data = ' + receive_message)
    print('=================================================')
    print('Client: ' + decrypt_message(receive_message, server_d, server_n))
    print('=================================================')

    
client.close()

