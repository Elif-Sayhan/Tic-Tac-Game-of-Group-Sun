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