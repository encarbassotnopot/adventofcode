#! /usr/bin/python
import os, re

lines = ""


with open(os.path.dirname(__file__) + "/input.txt") as f:
	lines = f.read()

lines = lines.split("\n\n")
cratesTxt = lines[0].splitlines()[:-1]
instructionsTxt = lines[1].splitlines()


crates = [[] for i in range(int((len(cratesTxt[0])+1)/4))]

for line in lines[0].splitlines()[:-1]:
	for index, i in enumerate(range(1, len(line), 4)):
		if (crate := line[i]) != " ":
			crates[index].append(crate)

[crate.reverse() for crate in crates]

instructions = [[int(i) for i in re.findall("\d+", line)] for line in instructionsTxt]

for instruction in instructions:
	ammount, origin, destination = instruction
	crates[destination-1] += crates[origin-1][-ammount:]
	del crates[origin-1][-ammount:]

print("".join([crate[-1] for crate in crates]))