from ttt_board import TTTBoard

def test_set_cell():
	board = TTTBoard()
	board.set_cell(1,0,0)
	board.set_cell(2,2,2)
	board.set_cell(1,2,0)
	print(board)

def test_make_move():
	board = TTTBoard()
	print(board)
	board.make_move()
	print(board)
	board.make_move()
	print(board)

def test_run_game():
	board = TTTBoard()
	board.run_game()

def main():
	test_run_game()

if __name__ == '__main__':
	main()
