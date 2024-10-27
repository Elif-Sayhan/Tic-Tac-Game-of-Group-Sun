# 1. Initialize the game board as a 3x3 grid
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]
    
# List of all possible winning combinations
win_positions = [
        # Horizontal wins
        [[0, 0], [0, 1], [0, 2]],  # First row
        [[1, 0], [1, 1], [1, 2]],  # Second row
        [[2, 0], [2, 1], [2, 2]],  # Third row
        # Vertical wins
        [[0, 0], [1, 0], [2, 0]],  # First column
        [[0, 1], [1, 1], [2, 1]],  # Second column
        [[0, 2], [1, 2], [2, 2]],  # Third column
        # Diagonal wins
        [[0, 0], [1, 1], [2, 2]],  # Diagonal from top-left to bottom-right
        [[0, 2], [1, 1], [2, 0]],  # Diagonal from top-right to bottom-left
    ]

 # "Ce code crée un plateau de jeu Tic-Tac-Toe en forme de grille 3x3, ce qui signifie qu'il a trois lignes et trois colonnes". 
 # "Chaque case sur la grille est un espace vide " ", où les joueurs peuvent faire leurs mouvements".

# 2. Keep track of players' moves
users = {
    "user1": [],  # List to store the moves of User 1 (X)
    "user2": [],  # List to store the moves of User 2 (O)
    "user1symbol": "X",
    "user2symbol": "O",
}

#"user1" :  les positions où le joueur 1 a placé son "X".
#"user2" :  les positions où le joueur 2 a placé son "O".

# 3. Function to display the current state of the board

def printBoard(users):
    print("-------")  # Print the top border of the board
    for i in range(len(board)):  # Loop through each row of the board
        print("|", end="")  # Print the left border of the row
        for j in range(len(board[i])):  # Loop through each column of the row
            if [i, j] in users["user1"]:  # Check if User 1 has made a move here
                print("X", end="|")  # If yes, print "X" for User 1's move
            elif [i, j] in users["user2"]:  # Check if User 2 has made a move here
                print("O", end="|")  # If yes, print "O" for User 2's move
            else:
                print(board[i][j], end="|")  # If no one has made a move, print an empty space
        print("\n-------")  # Print the bottom border of the row


# Function to verify the user's input for valid moves
def verifyInputofUser(row, column):
    allSteps = users["user1"] + users["user2"]  # Combine both players' moves
    if 0 <= row <= 9 and 0 <= column <= 9 and [row, column] not in allSteps:
        return True  # Valid input
    else:
        print("The spot is either out of range or already taken. Try again.")
        return False  # Invalid input
    
    #Est-ce que le numéro de la ligne est entre 0 et 9 ? 
    #Est-ce que le numéro de la colonne est entre 0 et 9 ? 
    #Est-ce que l'emplacement n'est pas déjà pris ? 
    #Si les trois conditions sont vraies, la fonction renvoie True, ce qui signifie que l'emplacement est bon à utiliser.

# 5. Function to check if a player has won the game
def checkWinner():
    for positions in win_positions:
        # Check if all positions in a line are filled by user1
        if all(pos in users["user1"] for pos in positions):
            print("User 1 (X) wins!")
            return True
        # Check if all positions in a line are filled by user2
        if all(pos in users["user2"] for pos in positions):
            print("User 2 (O) wins!")
            return True
    return False  # No winner yet

#La fonction checkWinner vérifie toutes les lignes gagnantes possibles sur le plateau. 
#Elle regarde si le joueur 1 ou le joueur 2 a rempli l'une de ces lignes. Si un joueur a gagné, elle annonce le gagnant et s'arrête. 
#Si personne n'a gagné, elle renvoie False.


# 6. Function to check if the game is a tie
def checkTie():
    # If all spots are filled and there is no winner, it's a tie
    if len(users["user1"]) + len(users["user2"]) == 9:
        print("It's a tie!")  # Announce tie
        return True  # Game is a tie
    return False  # Not a tie

#La fonction checkTie vérifie si tous les emplacements sur le plateau sont remplis et s'il n'y a pas de gagnant. 
# Si tous les emplacements sont remplis (9 mouvements au total), elle annonce un match nul et renvoie True. 
# Sinon, elle renvoie False, ce qui signifie que le jeu continue.



# 4. Function to ask the current user for their move
def demandPosition(player_number):
    check = True
    while check:  # Loop until a valid move is entered
        row = int(input(f"User {player_number}, enter the row number (0,1,..9): "))  # Get row input
        column = int(input(f"User {player_number}, enter the column number (0, 1,...9): "))  # Get column input
        if verifyInputofUser(row, column):  # Verify input
            users[f"user{player_number}"].append([row, column])  # Record the move
            check = False  # Exit loop on valid input
        else:
           check = True # Prompt to try again

# La fonction demandPosition demande à un joueur où il veut jouer (ligne et colonne). Elle vérifie si le mouvement est valide. 
# Si le mouvement est valide, elle enregistre le mouvement et arrête de demander. 
# Si le mouvement n'est pas valide, elle continue de demander jusqu'à ce que le joueur entre un mouvement valide.
# 7. Main game loop
print("Welcome to Tic-Tac-Toe!")  # Welcome message
printBoard(users)  # Print the initial board
turn = 1  # Keep track of the number of turns

while turn <= 9:  # Loop for a maximum of 9 turns
    # 8. Alternate between user 1 (odd turns) and user 2 (even turns)
    if turn % 2 == 1:
        demandPosition(1)  # User 1's turn
    else:
        demandPosition(2)  # User 2's turn

    # 9. Print the board after each turn
    printBoard(users)

    # 10. Check if there is a winner after each move
    if checkWinner():
        break  # Exit if there is a winner

    # 11. Check if it's a tie
    if checkTie():
        break  # Exit if the game is a tie

    # 12. Move to the next turn
    turn += 1  # Increment turn count


    #Ce code met en place une boucle pour un maximum de 9 tours dans un jeu de Tic-Tac-Toe.
    #  Il alterne entre l'utilisateur 1 et l'utilisateur 2, demandant leurs mouvements, 
    # imprimant le plateau, vérifiant s'il y a un gagnant et vérifiant s'il y a un match nul.
    #  Si un gagnant est trouvé ou si le jeu se termine par un match nul, la boucle s'arrête.
