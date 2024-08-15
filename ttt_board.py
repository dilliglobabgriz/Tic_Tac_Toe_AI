from typing import List

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

	def make_move(self) -> None:
		valid_move: bool = False
		move_coordinates: str = ''
		while not valid_move:
			move_coordinates = input(f'Player {self.turn} - select a square:')
			valid_move = True
		self.set_cell(self.turn, int(move_coordinates[0]), int(move_coordinates[1]))
		self.turn = 2 if self.turn == 1 else 1
		

	def is_board_full(self) -> bool:
		remaining_cells = 9
		for i in range(self.rows):
			for j in range(self.rows):
				if self.board[i][j] != 0:
					remaining_cells -= 1
		return remaining_cells == 0

	def run_game(self) -> None:
		while not self.is_board_full():
			print(self)
			self.make_move()
		print(self)
		print('It's a tie!')
		print('Thanks for playing :)'
