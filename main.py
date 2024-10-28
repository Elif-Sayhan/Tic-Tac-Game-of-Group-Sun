board = ["-","-","-",
         "-","-","-",
         "-","-","-"]


#Game Visuals 

#Game Start screen 
def game_start_screen(word):
    top_ = " /)__/)"+" "*2 +"*" * (len(word) + 4) + "(\\__(\\"+" "*3
    middle = "(='.'=)"+" "*2 +"* " + word + " *" + "(='.'=)"+" "*2
    bottom_ = "('')_('')"+"*" * (len(word) + 4) + "('')_('')"
    print(top_)
    print(middle)
    print(bottom_)


#Game Victory Screen 
def victory_screen(word,w):
    top_ = " /)__/)"+" "*2 +"*" * (len(word) + 4) + "(\\__(\\"+" "*3
    middle = "(='.'=)"+" "*2 +"* " + word + " *" + "(='.'=)"+" "*2
    bottom_ = "('')_('')"+"*" * (len(word) + 4) + "('')_('')"
    if w == "win":
        middle = middle[:3] + "w" + middle[3+1:]
        middle = middle[:len(word)+16] + "w" + middle[len(word)+17:]
    elif w == "lose":
        middle = middle[:3] + "^" + middle[3+1:]
        middle = middle[:len(word)+16] + "^" + middle[len(word)+17:]
    print(top_)
    print(middle)
    print(bottom_)

    #game board 
def print_board():
    first_row = "| " + board[0] + " | " + board[1] + " | " + board[2] + " |"
    second_row = "| " + board[3] + " | " + board[4] + " | " + board[5] + " |"
    third_row = "| " + board[6] + " | " + board[7] + " | " + board[8] + " |"
    separation_line = "-"*13
    print(first_row , separation_line , second_row , separation_line , third_row, sep = "\n")

    





#GAME FUNCTIONS 

#Player input modifies board ONLY if case is empty 
def player_move(index,move):
    if board[(index-1)] == "-":
        board[(index-1)] = move 
        print_board()
    elif board[(index-1)] == "X":
        board[(index-1)] = "X"
        return "Case is already played, pick an other one"
    elif board[(index-1)] == "O":
        board[(index-1)] = "O"
        return "Case is already played, pick an other one"

#Initialising functions for victory condition
def X_win(a,b,c):
    if board[a] == "X" and board[a] == board[b] and board [a] == board[c]:
        return "Win"
def O_lose(a,b,c):
    if board[a] == "O" and board[a] == board[b] and board [a] == board[c]:
        return "Lose"



#return victory, defeat or tie 
def victory_condition():
    if X_win(0,1,2) or X_win(3,4,5) or X_win(6,7,8) \
         or X_win(0,3,6) or X_win(1,4,7) or X_win(2,5,8) \
            or X_win(0,4,8) or X_win(2,4,6)== "Win":
        return "VICTORY"
    elif O_lose(0,1,2) or O_lose(3,4,5) or O_lose(6,7,8) \
         or O_lose(0,3,6) or O_lose(1,4,7) or O_lose(2,5,8) \
            or O_lose(0,4,8) or O_lose(2,4,6) == "Lose":
        return "DEFEAT"
    elif "-" not in board:
        return "TIE"



#check if victory_condition returns a value         
def true_false():
    if victory_condition() == "DEFEAT" or victory_condition() == "VICTORY" or victory_condition() == "TIE":
        return True
    else:
        return False 


#print victory_screen according to game result
def print_victory():
    if victory_condition() == "VICTORY":
        return victory_screen("VICTORY","win")
    elif victory_condition() == "DEFEAT":
        return victory_screen("DEFEAT","lose")
    elif victory_condition() == "TIE":
        return victory_screen("TIE","lose")





#BOT ALGORITHM 
#easy mode 
def easy_bot_move():
    i = 0
    for i in range (len(board)):
        if board[i] == "X" or board[i] == "O":
            i+=1
        elif board[i] == "-":
            board[i] = "O"
            break

#random mode 
import random
from random import randrange
def random_bot_move():
    for i in range(len(board)):
        i = randrange(len(board))
        if board[i] == "-":
            board[i] = "O"
            break
        elif board[i] == "X" or board[i] == "O":
            i = randrange(len(board))





#GAME RUN 

print(game_start_screen("GAME START_"))
print_board()
true_false()
while not true_false() == True:
    while True:
            try:
                case = int(input('case '))
                if case < 1 or case > 9:
                    raise ValueError #this will send it to the print message and back to the input option
                break
            except ValueError:
                print("Invalid integer. The input must be in the range of 1-9.")
    print(player_move(case,input("play ")))
    true_false()
    if true_false() == True:
        print (print_victory())
        break
    print(random_bot_move())
    print(print_board())
    true_false()
    if true_false() == True:
        print (print_victory())