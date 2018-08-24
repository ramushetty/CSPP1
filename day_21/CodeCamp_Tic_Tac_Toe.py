'''
GAME TIC TAC TOE
'''
BOARD = [0, 1, 2, 3, 4, 5, 6, 7, 8]
DUPLICATE = []
for loop in range(3):
    DUPLICATE.append(list(map(str, input().split())))
i = 0
for first in DUPLICATE:
    for element in first:
        BOARD[i] = element
        i += 1
def check_list(chaa, in1, in2, in3):
    '''
    checks the char in the given input
    '''
    if BOARD[in1] == chaa and BOARD[in2] == chaa and BOARD[in3] == chaa:
        return True
    return False
def  check(cha):
    '''
    returns true or false for each char
    '''
    if check_list(cha, 0, 1, 2):
        return True
    if check_list(cha, 0, 3, 6):
        return True
    if check_list(cha, 0, 4, 8):
        return True
    if check_list(cha, 3, 4, 5):
        return True
    if check_list(cha, 6, 7, 8):
        return True
    if check_list(cha, 1, 4, 7):
        return True
    if check_list(cha, 2, 5, 8):
        return True
    if check_list(cha, 6, 4, 2):
        return True
    return False
EMPTY = []
X_X = BOARD.count('x')
O_O = BOARD.count('o')
D_D = BOARD.count('.')
C_C = 0
S_S = 0
if X_X + O_O + D_D == 9:
    if abs(X_X - O_O) == 1:
        for char in BOARD:
            if char != '.':
                if check(char) == True:
                    S_S = 1
                    EMPTY.append(char)
        if S_S == 1:
            EMPTY = list(set(EMPTY))
            print(EMPTY[0])
        else:
            print("draw")
    else:
        C_C = 1
        print("invalid game")
else:
    if C_C != 1:
        print("invalid input")
