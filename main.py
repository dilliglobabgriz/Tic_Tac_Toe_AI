import sys
from ttt_board import TTTBoard
from ttt_ais.random_ai import RandomAi

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

def run_one_player_game(ai_type):
	board = TTTBoard()
	if ai_type == 'random':
		AI = RandomAi()
	board.run_game_one_player(AI)

def main():
	num_args = len(sys.argv)

	if num_args == 1:
		test_run_game()
	if num_args == 2:
		run_one_player_game(sys.argv[1])

if __name__ == '__main__':
	main()
