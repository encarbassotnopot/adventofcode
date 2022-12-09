#!/usr/bin/python

calories = []

with open("input.txt") as f:
	lines = f.readlines()
	sum = 0

	for line in lines:
		line = line.strip()
		if line == '':
			calories.append(sum)
			sum = 0
		else:
			sum += int(line)

top3 = [0, 0, 0]

for cal in calories:
	if cal > calories[2]:
		top3.append(cal)
		top3.sort(reverse=True)
		top3.pop()

print(top3[0])
print(top3[0] + top3[1] + top3[2])