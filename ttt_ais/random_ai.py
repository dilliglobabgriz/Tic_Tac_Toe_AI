from typing import List, Tuple
import random

class RandomAi():
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
		return random.choice(choices)
