from random_ai import RandomAi
from perfect_ai import PerfectAi


empty_board = [
	[0,0,0],
	[0,0,0],
	[0,0,0]
	]
board1 = [
	[0,0,1],
	[0,0,2],
	[0,0,0]
	]
board2 = [
	[0,1,2],
	[1,1,2],
	[2,1,0]
	]
board3 = [
	[2,0,1],
	[0,0,2],
	[1,1,2]
	]
board4 = [
	[1,2,1],
	[2,0,0],
	[0,0,0]
	]


def test_random():
	ai = RandomAi(board1, 1)
	print(ai.make_decision())

def test_perfect():
	ai = PerfectAi()
	print(ai.minimax_score(empty_board, 1, 1))

def main():
	test_perfect()

if __name__ == '__main__':
	main()
