#!/usr/bin/env python3

# python3 -m pip install pwntools
from pwn import *

# Paramètres de connexion
HOST, PORT = "challenges.france-cybersecurity-challenge.fr", 2052

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
	print("Début tri " + str(N)+" valeurs");
	positions = []
	for index in range(N):
		positions.append(index)
	positions = quicksort(positions, 2)
	print("Positions apres tri")
	printArray(positions)
	for index in range(N):
		if positions[index] != index:
			echanger(index, positions[index])
			# index --> positions[index]
			# on doit le modifier dans la liste
			#print("SWAP positions after index "+str(index))
			#printArray(positions)
			pos = positions.index(index)
			#print("POS "+str(pos)+" ["+str(positions[pos])+"] = "+str(positions[index]))
			positions[pos] = positions[index]
			positions[index] = -1 # do not use any more

	print("Fin Tri")

def quicksort(array, count):
	#print(" quicksort interation restantes "+str(count))
	#print("Positions avant tri")
	#printArray(array)
	N = len(array)
	if N < 2:
		return array
	
	pivotIndex = array[0]
	lessIndex = []
	greaterIndex = []

	index = 1
	while(index < N):
		if comparer(array[index], pivotIndex):
			lessIndex.append(array[index])
		else:
			#print(" GREATER "+str(array[index])+" than "+str(pivotIndex))
			greaterIndex.append(array[index]);
		index = index + 1
	#if (count > 1):
	return quicksort(lessIndex, 1) + [pivotIndex] + quicksort(greaterIndex, 1)
	#else:
	#	return lessIndex + [pivotIndex] + greaterIndex
	# 

def printArray(A):
	print(f"{A}")

# Ouvre la connexion au serveur
io = remote(HOST, PORT)

# Récupère la longueur du tableau
N = longueur()

# Appel de la fonction de tri que vous devez écrire
trier(N)

# Verification
verifier()

# Fermeture de la connexion
io.close()
