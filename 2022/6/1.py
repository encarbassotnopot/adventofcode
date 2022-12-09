#! /usr/bin/python
import os, re

string = []


with open(os.path.dirname(__file__) + "/input.txt") as f:
	string = [*f.read()]

lastChars = string[:4]

for index, char in enumerate(string[4:], 4):
	if len(set(lastChars)) == 4:
		print(index)
		break
	del lastChars[0]
	lastChars.append(char)