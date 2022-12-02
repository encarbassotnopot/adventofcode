#!/usr/bin/python

acumulat = 0

"""
A - Pedra	+1
B - Paper	+2
C - Tisores	+3
x - Perd	+0
Y - Empata	+3
Z - Guanya	+6
"""
def score_rps(elf, resultat):
	punts = 0

	if resultat == "X": # derrota
		if elf == "A":
			punts += 3 # tisores
		elif elf == "B":
			punts += 1 # pedra
		elif elf == "C":
			punts += 2 # paper

	elif resultat == "Y": # empat
		punts += 3
		if elf == "A":
			punts += 1 # pedra
		elif elf == "B":
			punts += 2 # paper
		elif elf == "C":
			punts += 3 # tisores

	elif resultat == "Z": # victòria
		punts += 6
		if elf == "A":
			punts += 2 # paper
		elif elf == "B":
			punts += 3 # tisores
		elif elf == "C":
			punts += 1 # pedra

	return punts


with open("input.txt") as f:
	for line in f.readlines():
		acumulat += score_rps(line[0], line[2])

print(acumulat)