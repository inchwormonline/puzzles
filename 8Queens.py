# This program find a solution for the n-Queens problem 
# for a given initial point when n = SIZE 
# The initial point is given as the input to fill_board(r,c)
# To find a correct solution r should be 0, but c can indeed has any value less than SIZE

SIZE = 8
board = []
queens = [SIZE for i in range(SIZE)]

def init_board():
    for i in range(SIZE):
		row = []
		for j in range(SIZE):
			row.append(SIZE)
		board.append(row)

def print_board():
	if SIZE == 1:
		print(board[0][0])
	else:
		for i in range(SIZE):
			print(board[i])
		print("----------------")

def put_queen(r,c):
	for i in range(c, SIZE):
		if board[r][i] == SIZE:
			board[r][i] = r;
			for j in range(r + 1, SIZE):
				board[j][i] = r
				if i + j - r < SIZE and board[j][i + j - r] == SIZE:
					board[j][i + j - r] = r
				if i - j + r >= 0 and board[j][i - j + r] == SIZE: 
					board[j][i - j + r] = r
			queens[r] = i
			return i
	return -1

def remove_queen(r):
	for k in range(r, SIZE):
		for i in range(r, SIZE):
			for j in range(0, SIZE):
				if board[i][j] == k:
					board[i][j] = SIZE
			queens[k] = SIZE
			
def fill_board(r, c):
	if r == SIZE-1: 
		if put_queen(r,c) > -1:
			return True
		# r == SIZE-1 and put_queen(r,c) == -1
		elif c == SIZE-1:
			return False
	else:
		if put_queen(r,c) > -1:
			if fill_board(r+1,0):
				return True
			else:
				q = queens[r]
				remove_queen(r)
				put_queen(r, q + 1)
				fill_board(r+1, 0)
		else: 
			if r > 1:
				q = queens[r-1]
				remove_queen(r-1)
				fill_board(r-1, q+1)
			else: 
				return False	
init_board()
fill_board(0,0)
if SIZE in queens:
	print("there is no solution with this initial point")
else:
	print(queens)