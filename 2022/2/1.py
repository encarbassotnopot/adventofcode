#!/usr/bin/python

acumulat = 0

"""
A, x - Pedra
B, Y - Paper
C, Z - Tisores
"""
def score_rps(elf, jugador):
	punts = 0
	if jugador == "X":
		punts += 1
		if elf == "A": # empat
			punts += 3
		elif elf == "C": # victòria
			punts += 6

	elif jugador == "Y":
		punts += 2
		if elf == "B": # empat
			punts += 3
		elif elf == "A": # victòria
			punts += 6

	elif jugador == "Z":
		punts += 3
		if elf == "C": # empat
			punts += 3
		elif elf == "B": # victòria
			punts += 6
	return punts


with open("input.txt") as f:
	for line in f.readlines():
		acumulat += score_rps(line[0], line[2])

print(acumulat)