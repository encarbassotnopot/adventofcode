#! /usr/bin/python
import os

total = 0

with open(os.path.dirname(__file__) + "/input.txt") as f:
	previ = int(f.readline())
	for line in f:
		actual = int(line.strip())
		if actual > previ:
			total += 1
		previ = actual

print(total)