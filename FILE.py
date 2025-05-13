'''
Created on Mar 21, 2025

@author: andyabu
'''

import random

def printBoard(board):
    print(board[0]+  "|"     + board[1] +    "|" + board[2])
    
    print(board[3]+  "|"+ board[4] + "|" + board[5])
   
    print(board[6]+  "|"+ board[7] + "|" + board[8])


def playerinput(board):
    slot = int(input(f"{players[firstplayer]}'s turn ({firstplayer}). Enter a number from 1-9: "))
    if slot>=1 and slot <=9 and board[slot-1]=="-":
        board[slot-1]=firstplayer
    else:
        print("my guy please pick a new spot")
    


def checkhorizontal(board):
    global winner 
    
    if board[0]==board[1]==board[2] and board[1]!="-":
        winner=board[1]
        return True
    elif board[3]==board[4]==board[5]and board[3]!="-":
        winner=board[3]
        return True
    elif  board[6]==board[7]==board[8]and board[6]!="-":
        winner=board[6]
        return True
    
def checkrow(board):
    global winner 
    if board[0]==board[3]==board[6] and board[0]!="-":
        winner=board[1]
        return True
    if board[1]==board[4]==board[7] and board[1]!="-":
        winner=board[1]
        return True
    if board[2]==board[5]==board[8] and board[2]!="-":
        winner=board[2]
        return True
def checkslanted(board):
    global winner 
    if board[0]==board[4]==board[8] and board[0]!="-":
        winner=board[4]
        return True
    if board[2]==board[4]==board[6] and board[2]!="-":
        winner=board[2]
        return True

def checktie(board):
    if "-" not in board:
        printBoard(board)
        print("no one won do you wnat to play aagin")
        gamerunning=False
    else:
        gamerunning = True
    return gamerunning
    
def checkWIN(board):
    if checkhorizontal(board) or checkrow(board) or checkslanted(board):
        print(f"The winner is {players[winner]}!")  # Use the player's name
        gamerunning = False
    else:
        gamerunning = True
    return gamerunning
    
# switch the player
def switchplayer():
    global firstplayer
    if firstplayer=="x":
        firstplayer="o"
    else:
        firstplayer="x"
    


def computer(board):
    while firstplayer=="o":
        position=random.randint(0,8)
        if board[position]=="-":
            board[position]="o"
            switchplayer()
            
            
board=["-","-","-",
       "-","-","-",
       "-","-","-"]
firstplayer="x"
winner=None

gamerunning=True

player1 = input("Enter Player 1's name (X): ")
player2 = input("Enter Player 2's name (O): ")
print(f"GET READY {player1} VS  {player2} ")
players = {"x": player1, "o": player2}
# printBoard(board) 

while gamerunning:
    printBoard(board)
    playerinput(board)
    gamerunning = checkWIN(board)
    if not gamerunning:
        break
    gamerunning = checktie(board)
    if not gamerunning:
        break
    switchplayer() 
    
    
    

