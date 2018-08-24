board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
dublicate = []
for loop in range(3):
	dublicate.append(list(map(str, input().split())))
i = 0
for first in dublicate:
	for element in first:
		board[i] = element
		i += 1
def check_list(char, in1, in2, in3):
	if board[in1] == char and board[in2] == char and board[in3] == char:
		return True
	return False
def  check(char):
	if check_list(char, 0, 1, 2):
		return True
	if check_list(char, 0, 3, 6):
		return True
	if check_list(char, 0, 4, 8):
		return True
	if check_list(char, 3, 4, 5):
		return True
	if check_list(char, 6, 7, 8):
		return True
	if check_list(char, 1, 4, 7):
		return True
	if check_list(char, 2, 5, 8):
		return True
	if check_list(char, 6, 4, 2):
		return True
empty = []
x_count = board.count('x')
o_count = board.count('o')
dot_count = board.count('.')
c_c = 0
s_s = 0
if x_count + o_count + dot_count == 9:
	if abs(x_count - o_count) == 1:
		for char in board:
			if char != '.': 
				if check(char) == True:
					s_s = 1
					empty.append(char)
		if s_s == 1:
			empty = list(set(empty))
			print(empty[0])
		else:
			print("draw")
	else:
		c_c = 1
		print("invalid game")
else:
	if c_c != 1:
		print("invalid input")



