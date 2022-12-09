#!/usr/bin/python
import os

sacks = []

with open(os.path.dirname(__file__)+"/input.txt") as f:
	sacks = f.read().splitlines()

items = []

for i in range(0, len(sacks), 3):
	items.append(list(set(sacks[i]).intersection(sacks[i+1]).intersection(sacks[i+2])))

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

priorities = [letters.index(item[0])+1 for item in items]

print(sum(priorities))