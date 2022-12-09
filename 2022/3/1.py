#!/usr/bin/python
import os

sacks = []

with open(os.path.dirname(__file__)+"/input.txt") as f:
	sacks = f.read().splitlines()


sacks = [[sack[:int(len(sack)/2)], sack[int(len(sack)/2):]] for sack in sacks]
items = [list(set(sack[0]).intersection(sack[1])) for sack in sacks]

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

priorities = [letters.index(item[0])+1 for item in items]

print(sum(priorities))