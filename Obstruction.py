

import random
import sys
from itertools import product

#Initializing Board
NUM_ROWS = 8
NUM_COLS = 8
board = []
player = [0, 1]
# Checker for player 1 is X and player 2 is O
for row in range(NUM_ROWS):
    row_list = []
    for col in range(NUM_COLS):
         row_list.append('.')
    board.append(row_list)
for i in range(ord('A'), ord('H') + 1):
        print('  ' + chr(i), end=' ')
print("\n +" + "---+" * NUM_COLS)
for row in range(NUM_ROWS):
        print(str(row) + '|', end=' ')
        for col in range(NUM_COLS):
            print(board[row][col] + ' | ', end='')
        print("\n +"+"---+"*NUM_COLS)

                 
# Function for printing board
def print_board():
    for i in range(ord('A'), ord('H') + 1):
        print('  ' + chr(i), end=' ')
    print("\n +" + "---+" * NUM_COLS)
    for row in range(NUM_ROWS):
            print(str(row) + '|', end=' ')
            for col in range(NUM_COLS):
                print(board[row][col] + ' | ', end='')
            print("\n +"+"---+"*NUM_COLS)
def win_indexes(n):
    # Rows
    indices=[]
    for row in range(n):
        indices.append([(row, col) for col in range(n)])
        
    # Columns
    for col in range(n):
        indices.append([(row, col) for row in range(n)])
        
    # Diagonal top left to bottom right
    indices.append([(i, i) for i in range(n)])
    
    # Diagonal top right to bottom left
    indices.append([(i, n - 1 - i) for i in range(n)])
    
    return indices

def det_winner(board, checker):
    n = len(board)
    for indexes in win_indexes(n):
        if all(board[row][col] == checker for row, col in indexes):
            return True
    return False

def det_tie(board):
    count = 0
    for a in range(NUM_ROWS):
        for b in range(NUM_COLS):
            
            if board[a][b] == "X" or board[a][b] == "O":
                count += 1
                return False
            if count == NUM_ROWS*NUM_COLS:
                print("The game ends in a Tie\n")
                return True

def neighbours(cell):
    for col in product(*(range(n-1, n+2) for n in cell)):
        if col != cell and all(0 <= n < NUM_ROWS for n in col):
            if board[col[0]][col[1]]=='.':
                board[col[0]][col[1]]='#'


# Randomly selecting a player
turn=random.choice(player)
win=False
while win==False: #Iterating the loop till any player wins or the game is a tie
    if turn==1:
        print('Player 1 chance')
        loc=input('Enter Checker location: ')
        checker='X'
    elif turn==0:
        print('Player 2 chance')
        loc=input('Enter Checker location: ')
        checker='O'
    location=[*loc]
    
#         Checks for invalid user input
        
    if len(location)>2: 
        print('Invalid location entered\nGame Ended')
        sys.exit()
        
    elif (ord(location[0]) not in range(ord('A'),ord('H') + 1) ) | (int(location[1])>=NUM_COLS):
        print('Invalid location entered\nGame Ended')
        sys.exit()
#         Check for invalid coordinates
    elif (board[int(location[1])][ord(location[0])-65]!='.') & (board[int(location[1])][ord(location[0])-65]!='#') :
        print('Already taken')
        continue
    else:
        board[int(location[1])][ord(location[0])-65]=checker
        neighbours((int(location[1]),ord(location[0])-65)) #Putting #'s in the neighbour of checker
        print_board()
    turn=(turn+1)%2            #Altering turn 
    if det_winner(board, 'O')==True: 
        print('Player 2 wins')
        win=True
    elif det_winner(board, 'X')==True:
        print('Player1 wins')
        win=True
    if det_tie(board)==True:
        sys.exit()
        
            
