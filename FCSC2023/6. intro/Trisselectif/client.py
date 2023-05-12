#!/usr/bin/env python3

# python3 -m pip install pwntools
from pwn import *

# Paramètres de connexion
HOST, PORT = "challenges.france-cybersecurity-challenge.fr", 2051

def comparer(x, y):
	io.sendlineafter(b">>> ", f"comparer {x} {y}".encode())
	return int(io.recvline().strip().decode())

def echanger(x, y):
	io.sendlineafter(b">>> ", f"echanger {x} {y}".encode())

def longueur():
	io.sendlineafter(b">>> ", b"longueur")
	return int(io.recvline().strip().decode())

def verifier():
	io.sendlineafter(b">>> ", b"verifier")
	r = io.recvline().strip().decode()
	if "flag" in r:
		print(r)
	else:
		print(io.recvline().strip().decode())
		print(io.recvline().strip().decode())

def trier(N):
	print("Début tri")
	index = 0
	highestOk = 0
	while (index < N-1):
		if comparer(index+1, index):
			echanger(index, index + 1)
			print("Position "+str(index)+" echangée")
			if index > 0:
				index = index - 1
		else:
			if index < highestOk:
				index = highestOk
			else:	
				highestOk = index
			index = index + 1			
	print("Fin Tri")	

# Ouvre la connexion au serveur
io = remote(HOST, PORT)
print("Connecté")	
# Récupère la longueur du tableau
N = longueur()
print("Longueur "+str(N))	

# Appel de la fonction de tri que vous devez écrire
trier(N)

# Verification
verifier()

# Fermeture de la connexion
io.close()
