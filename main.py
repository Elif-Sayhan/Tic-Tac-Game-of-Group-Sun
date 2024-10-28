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