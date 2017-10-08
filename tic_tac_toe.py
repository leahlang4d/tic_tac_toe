'''
Tic tac toe game against the computer
'''

def makegrid(board):
    print('     |      ')
    print(''+ board[7] + '  |   ' + ''+ board[8]+'  |   '+''+board[9])
    print('     |       ')
    print(''+ board[4]+ '   |   '+''+ board[5]+'    |    '+''+board[6])
    print('     |       ')
    print(''+ board[1]+ '   |   '+ ''+ board[2] +'  |   '+''+board[3])

def makeachoice():
    print("Welcome to Tic Tac Toe! Please Enter an X or O to get this game started!")
    letter = input().upper()
    if letter == 'X':
        print("You are X and the Computer will be O")
        return ['X','O']
    elif letter == 'O':
        print("You are O and the Computer will be X")
        return ['O', 'X']
    else:
        print("Please enter an X or O")


def comp_or_player_first( ):
    if random.randint(0,1) == 1:
        return 'player'
    else:
        return 'computer'


def play_again():
    print("Do you want to play again? (yes or no)")
    #starts with is used to check if a string starts with a certain string or character
    return input().lower().startswith('y')


def makeamove(board, move,letter):
    board[move] = letter

def is_winner(board_pos, play_lett):
    return((board_pos[7] == play_lett and board_pos[8] == play_lett and board_pos[9] == play_lett) or
           (board_pos[4] == play_lett and board_pos[5] == play_lett and board_pos[6] == play_lett) or
           (board_pos[1] == play_lett and board_pos[2] == play_lett and board_pos[3] == play_lett) or
           (board_pos[7] == play_lett and board_pos[5] == play_lett and board_pos[3] == play_lett) or #across from left
           (board_pos[9] == play_lett and board_pos[5] == play_lett and board_pos[1] == play_lett) or #across from right
           (board_pos[8] == play_lett and board_pos[5] == play_lett and board_pos[2] == play_lett))


