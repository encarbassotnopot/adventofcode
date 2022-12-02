#! /usr/bin/python
import os

total = 0

with open(os.path.dirname(__file__) + "/input.txt") as f:
	lines = f.readlines()
	ultim = int(lines[0]) + int(lines[1]) + int(lines[2])
	for a, b, c in zip(lines[1:], lines[2:], lines[3:]):
		print(a, b , c)
		actual = int(a) + int(b) + int(c)
		if actual > ultim:
			total += 1
		ultim = actual

print(total)