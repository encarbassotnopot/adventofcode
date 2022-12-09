#! /usr/bin/python
import os

def filtre(llista, num, pos):
	return [l for l in llista if l[pos] == num]

# oxygen meter
oxygen = 0
with open(os.path.dirname(__file__) + "/input.txt") as f:
	lines = [line.strip() for line in f.readlines()]

	for i in range(len(lines[0])):
		zeros = 0
		uns = 0

		for line in lines:
			bit = line[i]
			if bit == "0":
				zeros += 1
			elif bit == "1":
				uns += 1

		if uns >= zeros:
			lines = filtre(lines, "1", i)
		else:
			lines = filtre(lines, "0", i)

		if len(lines) == 1:
			oxygen = int(lines[0], base=2)
			break


# co2 meter
co2 = 0
with open(os.path.dirname(__file__) + "/input.txt") as f:
	lines = [line.strip() for line in f.readlines()]

	for i in range(len(lines[0])):
		zeros = 0
		uns = 0

		for line in lines:
			bit = line[i]
			if bit == "0":
				zeros += 1
			elif bit == "1":
				uns += 1

		if uns < zeros:
			lines = filtre(lines, "1", i)
		else:
			lines = filtre(lines, "0", i)

		if len(lines) == 1:
			co2 = int(lines[0], base=2)
			break

	

print(oxygen*co2)