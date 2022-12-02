#! /usr/bin/python
import os

horitzontal = 0
profunditat = 0
aim = 0

with open(os.path.dirname(__file__) + "/input.txt") as f:
	for line in f:
		if line.startswith("forward"):
			horitzontal += int(line.split(" ")[1])
			profunditat += int(line.split(" ")[1])*aim
		elif line.startswith("down"):
			aim += int(line.split(" ")[1])
		elif line.startswith("up"):
			aim -= int(line.split(" ")[1])

print(horitzontal*profunditat)