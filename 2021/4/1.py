#!/usr/bin/python
import os

numbers = []
cards = []

def update_cards(cards: list, ball: int):
	return [[[(number[0], number[0] == ball or number[1]) for number in line] for line in card] for card in cards]

def check_bingo(cards: list):
	for card_num in range(len(cards)):
		card = cards[card_num]
		
		# horitzontal
		for line in card:
			bingo = True
			for n, check in line:
				bingo = bingo and check
			if bingo:
				return card_num

		# vertical
		for i in range(len(card[0])):
			bingo = True
			for j in range(len(card)):
				bingo = bingo and card[j][i][1]
			if bingo:
				return card_num

def sum_unmarked(card):
	sum = 0
	for line in card:
		for num, checked in line:
			if(not checked):
				sum += num
	return sum

with open(os.path.dirname(__file__) + "/input.txt") as f:
	numbers = f.readline().strip().split(",")
	numbers = [int(number) for number in numbers]

	cards = f.read().split("\n\n")
	cards = [card.splitlines() for card in cards]
	cards = [[line.split() for line in card if line != ""] for card in cards]
	cards = [[[(int(number), False) for number in line] for line in card] for card in cards]

for number in numbers:
	cards = update_cards(cards, number)
	if (index:= check_bingo(cards)):
		print(number*sum_unmarked(cards[index]))
		break
