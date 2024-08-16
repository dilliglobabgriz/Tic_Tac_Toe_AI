from random_ai import RandomAi
from perfect_ai import PerfectAi

board1 = [
	[0,1,2],
	[1,0,2],
	[2,1,0]
	]
board2 = [
	[0,1,2],
	[1,1,2],
	[2,1,0]
	]

def test_random():
	ai = RandomAi(board1, 1)
	print(ai.make_decision())

def test_perfect():
	ai = PerfectAi()
	ai.set_board(board2)
	print(ai.minimax_score())

def main():
	test_perfect()

if __name__ == '__main__':
	main()
