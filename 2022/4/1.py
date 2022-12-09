#! /usr/bin/python
import os

values = []
contained = 0

with open(os.path.dirname(__file__) + "/input.txt") as f:
	for line in f:
		line = line.strip()
		values += [[[int(element) for element in pair.split("-")] for pair in line.split(",")]]

for pair in values:
	if pair[0][0] >= pair[1][0] or pair[0][1] <= pair[1][1]:
		contained += 1
	elif pair[1][0] >= pair[0][0] or pair[1][1] <= pair[0][1]:
		contained += 1

print(contained)