from typing import List, Tuple
import random

class FindWinAi():
	def __init__(self):
		self.board = [[]]
		self.turn = 1
	
	def set_board(self, board: List[List[int]]) -> None:
		self.board = board

	def set_turn(self, turn: int) -> None:
		self.turn = turn

	def make_decision(self) -> Tuple[int, int]:
		choices: List[Tuple[int, int]] = []
		for row in range(3):
			for col in range(3):
				if self.board[row][col] == 0:
					choices.append((row, col))
			
		if self.find_winning_move(choices) != (-1, -1):
			return self.find_winning_move(choices)
		else: 
			return random.choice(choices)

	def find_winning_move(self, choices: List[Tuple[int, int]]) -> Tuple[int, int]:
		for choice in choices:
			temp_board = [row[:] for row in self.board]
			temp_board[choice[0]][choice[1]] = self.turn
			if self.has_three_in_a_row(self.turn, temp_board):	
				return choice
		return (-1, -1)

	def has_three_in_a_row(self, value, board):
		# Horizontal check
		for row in board:
			if row.count(value) == 3:
				return True
 
		# Vertical check
		for col in range(3):
			 if [board[i][col] for i in range(3)].count(value) == 3:
				 return True

		# Diagonals
		if [board[i][i] for i in range(3)].count(value) == 3:
			return True

		if [board[i][2-i] for i in range(3)].count(value) == 3:
			return True


		# Default
		return False	
