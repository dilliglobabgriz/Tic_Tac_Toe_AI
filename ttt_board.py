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
		x_coord = '-1'
		y_coord = '-1'
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
		return remaining_cells == 0

	def is_winner(self) -> bool:
		return False

	def run_game(self) -> None:
		while not self.is_board_full():
			print(self)
			self.make_move(self.get_coords())
		print(self)
		print("It's a tie!")
		print('Thanks for playing :)')
