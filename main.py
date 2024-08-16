from typing import List
import sys
from ttt_board import TTTBoard
from ttt_ais.random_ai import RandomAi
from ttt_ais.find_win_ai import FindWinAi
from ttt_ais.find_win_and_loss_ai import FindWinAndLossAi

def get_ai_object(ai_name: str):
	if ai_name == 'random':
		AI = RandomAi()
		return AI
	elif ai_name == 'findwin':
		AI = FindWinAi()
		return AI
	elif ai_name == 'fwal':
		AI = FindWinAndLossAi()
		return AI
	else:
		print('Sorry this arg is not recognized')

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
	AI = get_ai_object(ai_type)
	board.run_game_one_player(AI)

def run_zero_player_game(ai_type1: str, ai_type2: str) -> int:
	board = TTTBoard()
	AI1 = get_ai_object(ai_type1)
	AI2 = get_ai_object(ai_type2)
	board.run_game_zero_player(AI1, AI2)

def get_result_zero_player(ai_type1: str, ai_type2: str) -> int:
	board = TTTBoard()
	AI1 = get_ai_object(ai_type1)
	AI2 = get_ai_object(ai_type2)
	return(board.get_result_zero_player(AI1, AI2))

def run_sim() -> None:
	# List order is ties, 1 wins, 2 wins
	ai_wins_list = [0,0,0]
	# Each iteration run two games so each player can go first
	for i in range(int(sys.argv[3])):
		game_one_result = get_result_zero_player(sys.argv[1], sys.argv[2])
		ai_wins_list[game_one_result] += 1
		game_two_result = get_result_zero_player(sys.argv[2], sys.argv[1])
		
		# For game two we switch p1 and p2 so we adjust our counter accordingly
		if game_two_result == 1:
			ai_wins_list[2] += 1
		elif game_two_result == 2:
			ai_wins_list[1] += 1
		else:
			ai_wins_list[0] += 1
		
	display_results(ai_wins_list)

# Takes a list of three ints [ties, p1wins, p2wins]
def display_results(results: List[int]):	
	print(f'Ties: {results[0]}')
	if sys.argv[1] != sys.argv[2]:
		print(f'{sys.argv[1]} AI wins: {results[1]}')
		print(f'{sys.argv[2]} AI wins: {results[2]}')
	# If AIs are the same create a way to distinguish
	else:
		print(f'{sys.argv[1]}(1) AI wins: {results[1]}')
		print(f'{sys.argv[2]}(2) AI wins: {results[2]}')
			


def main():
	num_args = len(sys.argv)

	if num_args == 1:
		test_run_game()
	if num_args == 2:
		run_one_player_game(sys.argv[1])
	if num_args == 3:
		run_game_zero_player(sys.argv[1], sys.argv[2])
	if num_args == 4:
		run_sim()


if __name__ == '__main__':
	main()
