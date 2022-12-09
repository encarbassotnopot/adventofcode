#! /usr/bin/python
import os

bits = []
gamma = 0b0

with open(os.path.dirname(__file__) + "/input.txt") as f:
	bits.extend([0 for i in range(len(f.readline().strip()))])
	lines = f.readlines()
	for line in lines:
		for pos, bit in enumerate(line):
			if bit == "1":
				bits[pos] += 1

	gamma = int("".join(["1" if bit > len(lines)/2 else "0" for bit in bits]), base=2)
	epsilon = int("".join(["1" if bit <= len(lines)/2 else "0" for bit in bits]), base=2)

print(gamma*epsilon)