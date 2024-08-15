from random_ai import RandomAi

board1 = [[0,1,2],[1,0,2],[2,1,0]]

def test_random():
	ai = RandomAi(board1, 1)
	print(ai.make_decision())

def main():
	test_random()

if __name__ == '__main__':
	main()
