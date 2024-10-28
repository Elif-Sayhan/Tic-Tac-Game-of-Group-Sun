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