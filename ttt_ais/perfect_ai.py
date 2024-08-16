from typing import List, Tuple
import random

class PerfectAi():

	def __init__(self):
		self.board = [[]]
		self.turn = 1
	
	def set_board(self, board: List[List[int]]) -> None:
		self.board = board

	def set_turn(self, turn: int) -> None:
		self.turn = turn

	def swap_turn(self) -> None:
		self.turn = 3 - self.turn

	def get_player_choices(self, player: int) -> List[Tuple[int, int]]:
		choices: List[Tuple[int, int]] = []
		for row in range(3):	
			for col in range(3):
				if self.board[row][col] == 0:
					choices.append((row, col))
		return choices

	# Return the value of the currrent board state for the current player 
	# -10 means current player lost
	# 0 means game is a tie
	# 10 means current player won
	def minimax_score(self) -> int:
		# Determine is game is in terminal state
		if self.has_three_in_a_row(self.turn, self.board):	
			return 10
		if self.has_three_in_a_row(3 - self.turn, self.board):	
			return -10
		elif self.get_player_choices(1) == []:
			return 0
		return -1
		
					
		# Starting from terminal states, recurse backwards making the best moves for each player
		# If a non-terminal state leads to a terminal state with perfect play, that state should be treated as terminal
		legal_moves: List[Tuple[int, int]] = get_player_choices(self.turn)		


	def make_decision(self) -> Tuple[int, int]:
		my_choices: List[Tuple[int, int]] = self.get_player_choices(self.turn)

		opponent_choices: List[Tuple[int, int]] = self.get_player_choices(3 - self.turn)
	
		
		if self.find_winning_move(my_choices, self.turn) != (-1, -1):
			return self.find_winning_move(my_choices, self.turn)
		elif self.find_winning_move(opponent_choices, 3 - self.turn) != (-1, -1):
			return self.find_winning_move(opponent_choices, 3 - self.turn)
		else: 
			return random.choice(my_choices)

	def find_winning_move(self, choices: List[Tuple[int, int]], player: int) -> Tuple[int, int]:
		for choice in choices:
			temp_board = [row[:] for row in self.board]
			temp_board[choice[0]][choice[1]] = player
			if self.has_three_in_a_row(player, temp_board):	
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
