board = ["   " for i in range(9)]
result  = "game on"
def isDraw():
      if "   " not in board:
         print("Game Draw")
         result = "draw"
         exit()

def p1_isWon():
    if board[0] == " X " and board[1] == " X " and board[2] == " X " or \
       board[3] == " X " and board[4] == " X " and board[5] == " X " or \
       board[6] == " X " and board[7] == " X " and board[8] == " X " or \
       board[0] == " X " and board[3] == " X " and board[6] == " X " or \
       board[1] == " X " and board[4] == " X " and board[7] == " X " or \
       board[2] == " X " and board[5] == " X " and board[8] == " X " or \
       board[0] == " X " and board[4] == " X " and board[8] == " X " or \
       board[2] == " X " and board[4] == " X " and board[6] == " X " :
              print("Player 1 (X) Won, Congrats")
              global result
              result ="won"
              

##### function for player 1 move X player

#########
def p2_isWon():
    if board[0] == " O " and board[1] == " O " and board[2] == " O " or \
       board[3] == " O " and board[4] == " O " and board[5] == " O " or \
       board[6] == " O " and board[7] == " O " and board[8] == " O " or \
       board[0] == " O " and board[3] == " O " and board[6] == " O " or \
       board[1] == " O " and board[4] == " O " and board[7] == " O " or \
       board[2] == " O " and board[5] == " O " and board[8] == " O " or \
       board[0] == " O " and board[4] == " O " and board[8] == " O " or \
       board[2] == " O " and board[4] == " O " and board[6] == " O " :
              print("Player 2 (O) Won, Congrats")
              global result
              result ="won"
              
              

##### function for player 1 move X player 

###### FUNCTION FOR printing board

def print_board():
    
    row1 = "|{}|{}|{}|".format(board[0],board[1],board[2])
    row2 = "|{}|{}|{}|".format(board[3],board[4],board[5])
    row3 = "|{}|{}|{}|".format(board[6],board[7],board[8])

    print("### Welcome to OBIE Tic Tac Toe ###")
    print(row1)
    print(row2)
    print(row3)
    print("####################################")
    p1_isWon()
    p2_isWon()
    if result != "won":
       isDraw()
       
       
###########

#########




def player1():
    if result == "game on" and result != "draw":
       choice = int(input("Enter your move player 1 (1-9):").strip())
       if board[choice-1]== "   ":
          board[choice-1]=" X "
       else:
          print("Sorry, space is taken")
          player1()
######



##### function for player 2 move O player 

def player2():
    if result == "game on" and result != "draw":
       choice = int(input("Enter your move player 2(1-9):").strip())
       if board[choice-1]== "   ":
          board[choice-1]=" O "
       else:
           print("Sorry, space is taken")
           player2()
######

while result == "game on":
         print_board()
         player1()
         print_board()
         player2()
      
      
      
