from random import randrange


def display_board(board):
    for row in board: #Searches each element in board list

    #Weird print but prints out one row of the tictactoe
        print("""   
+-------+-------+-------+
|       |       |       |
|   """,row[0],"""   |   """,row[1],"""   |   """,row[2],"""   |
|       |       |       |
""", sep="", end="+-------+-------+-------+")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    valid_move = False

    while valid_move == False:

        move = int(input("\nEnter your move: "))
        
        if move > 0 and move < 10: #checks if move is valid, if it's not goes to else statement
            for row in board:
                for elem in range(len(row)):
                    if row[elem] == move:
                        row[elem] = "O"
                        valid_move = True
                        break
                if valid_move:
                    break
            else:
                print("It's not hard to get the rules of the game")
                
                
        else:
            print("\nI told you not to try any funny stuff.")                   
            





def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.

    free_fields = []
    
    for row in range(3):
        for elem in range(3):
            if board[row][elem] != "O" and board[row][elem] != "X":
                free_fields.append((row, elem))


    return free_fields




def victory_for(board, sign):
    # The function analyzes the board's status in order to check if someone has won
    # Sign parameter is for the function to determine individually if X or O won, so its value will always be either "X" or "O"

    #These checks the 3 in col Win condition
    if board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        return True
    elif board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        return True
    elif board[0][2] == sign and board[1][2] == sign and board[2][2] == sign: 
        return True
    #These check the 3 cross Win Condition
    elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign: 
        return True
    elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign: 
        return True
    else: #This is to see the case of 3 in a row Win
        for row in board:
            if row[0] == sign and row[1] == sign and row[2] == sign:
                return True
                break
            

def draw_move(board):
    # The function draws the computer's move and updates the board.
    free_fields = make_list_of_free_fields(board)
    cycle_stopper = False
    
    while cycle_stopper == False: #Cycle will only stop when the randomnumberpicker picks a value that's free in the board

        random_number_picker = (randrange(0, 3), randrange(0, 3))
        
        for positions in free_fields:
            if random_number_picker == positions:
                row = random_number_picker[0]
                col = random_number_picker[1]
             
                board[row][col] = "X"
                cycle_stopper = True
                break
    
    



#Functions up, Main code below -------------------------------------------------------------------------------


board = [[1, 2, 3],[4, "X", 6],[7, 8, 9]]


print("""Welcome to the TicTacToe game, the game will
ask you to make a move and you can make your
move in the spaces where there is a number.\n
You will play as O and the computer will play as X.\n
Also if you try any funny stuff the game will
end immediatly.\n
That's All. Good Luck!
      """)

while True:
    display_board(board)
    
    enter_move(board)

    victory_computer = victory_for(board, "X")
    victory_user = victory_for(board, "O")
    draw = make_list_of_free_fields(board)

    if(victory_computer == True):
        print("Computer won the game!")
        break
    elif(victory_user == True):
        print("User won the game!")
        break
    elif(draw == []):
        print("It's a draw!")
        break

    draw_move(board)

    victory_computer = victory_for(board, "X")
    victory_user = victory_for(board, "O")
    draw = make_list_of_free_fields(board)

    if(victory_computer == True):
        print("Computer won the game!")
        break
    elif(victory_user == True):
        print("User won the game!")
        break
    elif(draw == []):
        print("It's a draw!")
        break
    






    
