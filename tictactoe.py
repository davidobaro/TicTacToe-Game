import os
import random

winner = 'j'

def rowChecker(a):
    threeInARow = 0
    global winner
    for p in range(0, len(a),2):
        for i in range(0, len(a[p]), 2):
            if i==0 and (a[p][i] == 'X' or a[p][i] == 'O'):
                threeInARow +=1

            if i > 1:
                if  a[p][i] == a[p][i-2] and (a[p][i] == 'X' or a[p][i] == 'O'):
                    threeInARow += 1
            
            if threeInARow == 3:
                winner = a[p][i]
                return True

        threeInARow = 0
    return False

def colChecker(a):
    threeInARow = 0
    global winner
    for p in range(0, len(a),2):
        for i in range(0, len(a[p]), 2):
            if i==0 and (a[i][p] == 'X' or a[i][p] == 'O'):
                threeInARow +=1

            if i>1:
                if a[i-2][p] == a[i][p] and (a[i][p] == 'X' or a[i][p] == 'O'):
                    threeInARow += 1
                    
            if threeInARow == 3:
                winner = a[i][p]
                return True
            
        threeInARow = 0
    return False

def diagChecker(a):
    global winner

    if a[0][0] == a[2][2] == a[4][4]:
        winner = a[2][2]
        return True
    
    if a[0][4] == a[2][2] == a[4][0]:
        winner = a[2][2]
        return True
    return False


board = [['1','|','2','|','3'],
         ['—','—','—','—','—'],
         ['4','|','5','|','6'],
         ['—','—','—','—','—'],
         ['7','|','8','|','9']]

valid_moves = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


os.system('cls')
print(
'''
  _______ _          _______             _______         
 |__   __(_)        |__   __|           |__   __|        
    | |   _  ___ ______| | __ _  ___ ______| | ___   ___ 
    | |  | |/ __|______| |/ _` |/ __|______| |/ _ \ / _ \\
    | |  | | (__       | | (_| | (__       | | (_) |  __/
    |_|  |_|\___|      |_|\__,_|\___|      |_|\___/ \___|      by David Obaro
'''
        )

print("-------------------------------------------------------------")

for line in board:
    print("                       ", end = " ")
    print(*line)

print("-------------------------------------------------------------")

decider = random.randint(0, 1)
if decider == 0:
    print("X begins...")

else:
    print("O begins...")

count = 1
move = '1'

while not( colChecker(board) or rowChecker(board) or diagChecker(board) or count>9): 
    
    if decider%2 == 0:
        print ("round " + str(count))
        print(
'''
             __   __
             \ \ / /
              \ V / 
               > <  's turn to play
              / . \ 
             /_/ \_\\
'''
        )
        print("---------------------------------------------------------------")
        move = input("Type the number representing the box you want to play on: ")

        while move not in valid_moves:
            move = input("Invalid move! Please type a number from the available options: ")

        valid_moves.remove(move)
        
        for p in range(0, len(board),2):
            for i in range(0, len(board[p]), 2):
                curr  = board[p][i]
                if board[p][i] == move:
                    board[p][i] = 'X'
                    break

    if decider%2 == 1: 
        print ("round " + str(count))
        print(
'''
              ____  
             / __ \ 
            | |  | |
            | |  | |'s turn to play
            | |__| |
             \____/     
'''
            )
        print("---------------------------------------------------------------")
        
        move =  input("Type the number representing the box you want to play on: ")

        while move not in valid_moves:
            move = input("Invalid move! Please type a number from the available options: ")

        valid_moves.remove(move)
        
        for p in range(0, len(board),2):
            for i in range(0, len(board[p]), 2):
                if board[p][i] == move:
                    board[p][i] = 'O'
                    break
    decider +=1
    count+= 1
    os.system('cls')

    print(
'''
  _______ _          _______             _______         
 |__   __(_)        |__   __|           |__   __|        
    | |   _  ___ ______| | __ _  ___ ______| | ___   ___ 
    | |  | |/ __|______| |/ _` |/ __|______| |/ _ \ / _ \\
    | |  | | (__       | | (_| | (__       | | (_) |  __/
    |_|  |_|\___|      |_|\__,_|\___|      |_|\___/ \___|      by David Obaro
'''
        )
    
    print("---------------------------------------------------------------")
    for line in board:
        print("                       ", end = " ")
        print(*line)
                
                
    print("---------------------------------------------------------------")

if (colChecker(board) or rowChecker(board) or diagChecker(board)):
    print("We have a Winner...")
    if winner == 'X':
        print(
'''
             __   __
             \ \ / /
              \ V / 
               > <  wins!
              / . \ 
             /_/ \_\\
'''
            )
        

    elif winner == 'O':
        print(
'''
              ____  
             / __ \ 
            | |  | |
            | |  | | wins!
            | |__| |
             \____/ 
''')

elif (count > 9):
    print("It's a Draw!")
