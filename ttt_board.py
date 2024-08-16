from typing import List, Tuple

class TTTBoard():
	def __init__(self):
		self.board: List[List[int]] = [[0,0,0],[0,0,0],[0,0,0]]
		self.rows: int = 3
		self.turn: int = 1

	def __str__(self) -> str:
		board_str = ''
		board_str += self.get_row_string(0)
		board_str += f'---|---|---\n'
		board_str += self.get_row_string(1)
		board_str += f'---|---|---\n'
		board_str += self.get_row_string(2)
		return board_str

	def swap_turn(self) -> None:
		self.turn = 1 if self.turn == 2 else 1

	def get_row_string(self, row: int) -> str:
		row_vals: List[int] = self.board[row]
		return f' {self.get_symbol(row_vals[0])} | {self.get_symbol(row_vals[1])} | {self.get_symbol(row_vals[2])} \n'
				
	def get_symbol(self, cell: int) -> str:
		if cell == 1:
			return 'X'
		elif cell == 2:
			return 'O'
		else:
			return ' '

	def set_cell(self, value: int, row: int, col: int) -> None:
		self.board[row][col] = value

	# Return a tuple of ints
	def get_coords(self) -> Tuple[int, int]: 
		x_coord = input(f'Player {self.turn} enter your desired row (0-2):')
		y_coord = input(f'Player {self.turn} enter your desired column (0-2):')
		while not self.are_valid_coords(x_coord, y_coord):
			x_coord = input(f'Player {self.turn} enter your desired row (0-2):')
			y_coord = input(f'Player {self.turn} enter your desired column (0-2):')
		
		return (int(x_coord), int(y_coord))
	
	def are_valid_coords(self, x_coord: str,  y_coord: str) -> bool:
		if x_coord not in '012' or y_coord not in '012':
			print('Inputs must be either 0, 1, or 2!')
			return False
		if self.board[int(x_coord)][int(y_coord)] != 0:
			print('This square is already taken!')
			return False
		return True	

	# Coordinates is a tuple of ints
	def make_move(self, coordinates: Tuple[int, int]) -> None:
		self.set_cell(self.turn, coordinates[0], coordinates[1])
		self.turn = 2 if self.turn == 1 else 1
		

	def is_board_full(self) -> bool:
		remaining_cells = 9
		for i in range(self.rows):
			for j in range(self.rows):
				if self.board[i][j] != 0:
					remaining_cells -= 1
		#if remaining_cells == 0:
			#print("It's a tie!")
			
		return remaining_cells == 0

	def is_winner(self) -> bool:
		if self.has_three_in_a_row(1) or self.has_three_in_a_row(2):
			self.turn = 2 if self.turn == 1 else 1
			#print(f'Player {self.turn} wins!')
			return True
		return False

	def get_winner(self) -> int:
		if self.has_three_in_a_row(1):
			return 1
		elif self.has_three_in_a_row(2):
			return 2
		else:
			return -1

	def has_three_in_a_row(self, value):
		# Horizontal check
		for row in self.board:	
			if row.count(value) == self.rows:
				return True

		# Vertical check
		for col in range(self.rows):
			if [self.board[i][col] for i in range(self.rows)].count(value) == self.rows:
				return True
		
		# Diagonals
		if [self.board[i][i] for i in range(self.rows)].count(value) == self.rows:
			return True

		if [self.board[i][2-i] for i in range(self.rows)].count(value) == self.rows:
			return True	
			
	
		# Default
		return False

	def run_game(self) -> None:
		while not self.is_winner() and not self.is_board_full():
			print(self)
			self.make_move(self.get_coords())
		print(self)
		print('Thanks for playing :)')

	def run_game_one_player(self, ai) -> None:
		while not self.is_winner() and not self.is_board_full():
			print(self)
			if self.turn == 1:
				self.make_move(self.get_coords())
			else:
				ai.board = self.board
				ai.turn = self.turn
				self.make_move(ai.make_decision())

		print(self)
		print('Thanks for playing :)')

	def run_game_zero_player(self, ai1, ai2) -> None:
		while not self.is_winner() and not self.is_board_full():
			print(self)
			if self.turn == 1:
				ai1.board = self.board
				ai1.turn = self.turn
				self.make_move(ai1.make_decision())
			else:
				ai2.board = self.board
				ai2.turn = self.turn
				self.make_move(ai2.make_decision())
		print(self)
	
	# Plays a full game between 2 ais and returns the winner (1 or 2)
	def get_result_zero_player(self, ai1, ai2) -> int:
		while not self.is_winner() and not self.is_board_full():
			if self.turn == 1:
				ai1.board = self.board
				ai1.turn = self.turn
				self.make_move(ai1.make_decision())
			else:
				ai2.board = self.board
				ai2.turn = self.turn
				self.make_move(ai2.make_decision())
		if self.is_winner():
			return self.get_winner()
		else: 
			return 0	
