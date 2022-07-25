################################################################################
# Jonah Fullen | Oct. 14, 2019
# CSC-131-005
# Programming Assignment 4.3: Battleship
"""
[Comment to the TA]
Ganga, 
I did not use the framework for any of this assignment. At no point did the
directions say that we must use it but always said something like 'if you
weren't able to do the previous part here is the framewoek for it.' I have
already spoken with Dr. Dogan about this and have assured her that I hace not
taken any of my cade from the internet but have written it all myself - and I
believe taht all of my comments throughout the code will show this as well.
After briefly looking at my code, Dr. Dogan has said that it is okay for me
to not redo the entire assignment with the framework, but that I can keep my
own version of the program.
"""

"""
NOTE: BECAUSE I DID NOT USE THE FRAMEWORK MY GAME DOES NOT PLAY EXACTLY LIKE
THE FRAMEWORK VERSION. PAY ATTENTION TO THE ON-SCREEN DIRECTIONS TO PLAY.
"""

# Purpose: This program is a working version of the game battleship. It contains
#       differing levels of difficulty that determine the size of the board to
#       play on. The game only allows one player to play against a computer that
#       is controlled by pure randomization - no AI functionality. Once the game
#       is over - either all of the computer's or player's ships have been
#       sunk - the program offers the user the option to restart and play the
#       game again. 
# Function Descriptions: appear in order of usage
#   board(Level): This function calculated the size of the gameboard
#       based on the input Level of difficulty given by the user within main()
#       Returns: Boardsize - an integer
#   displayBoard(Gameboard): This function gbuilds the gameboard based off of
#       the Boardsize.
#       Returns: FullBoard - a nested list where each list represents the
#           corresponding row on the board.
#   printBoard(Level, FullBoard): This function takes the level (board size)
#       and the FullBoard (the current layout of the gameboard) and prints
#       the board for the user to see.
#       Returns: none
#   placeAC(Level, FulBoard): This funciton takes the Level (board size) and
#       the current FullBoard and works with the user to place their Aircraft
#       Carrier ship that is 5 spaces long.
#       Returns: ACLocation - a nested list where each list represents a space
#           on the board that the Aircraft Carrier takes up - 5 items long
#   placeBattleship(Level, FullBoard): This funciton takes the Level (board
#       size) and the current FullBoard and works with the user to place their
#       Battleship ship that is 4 spaces long.
#       Returns: BattleshipLocation - a nested list where each list represents
#           a space on the board that the Battleship takes up - 4 items long
#   placeCruiser(Level, FulBoard): This funciton takes the Level (board size)
#       and the current FullBoard and works with the user to place their
#       Cruiser ship that is 3 spaces long.
#       Returns: CruiserLocation - a nested list where each list represents a
#           space on the board that the Cruiser takes up - 3 items long
#   placeSub(Level, FullBoard): This funciton takes the Level (board size)
#       and the current FullBoard and works with the user to place their
#       Submarine ship that is 3 spaces long.
#       Returns: SubLocation - a nested list where each list represents a
#           space on the board that the Submarine takes up - 3 items long
#   placeDestroyer(Level, FullBoard): This funciton takes the Level (board size)
#       and the current FullBoard and works with the user to place their
#       Destroyer ship that is 2 spaces long.
#       Returns: DestroyerLocation - a nested list where each list represents a
#           space on the board that the Destroyer takes up - 2 items long
#   computerShipPlacement(FullBoard): This function uses random to place the
#       computer's ships on the board without displaying their location to the
#       player.
#       Returns: CompAC, CompBattleship, CompCruiser, CompSub, and
#           CompDestroyer. Each is a nested list that represents the
#           corresponding ship's location on the board.
#   playerGuess(CompShipPlaces, CompShips, FullBoard): This function takes a
#       user input location on the board and bombs that location after checking
#       its validity.
#       Returns: CompShipPlaces - a nested list containing the locations of the
#           computer's ships. CompShips - an integer representing the number of
#           ship places the comuter has left on the board. FullBoard - the board
#           but edited to display the bombed location. 
#   computerGuess(PlayerShips, FullBoard): This function randomly generates a
#       location on the board to bomb and determines if that location is the
#       position of one of the player's ships.
#       Returns: PlayerShips - an integer representing the number of ship spaces
#           that the player has left before thry lose. FullBoard - this has been
#           changed to display the hit or missed location of the bombing. 
#   main(): This function controls the general interface and operation of the
#       program and calls all of the other functions.
#####
####
###
##
#
import random

def board(Level):
    BoardSize = 10
    if Level > 2:
        BoardSize += (Level - 1) * 2
    elif Level == 2:
        BoardSize += 2
    return BoardSize
        
def displayBoard(Gameboard):
    # This generates the .'s and *'s for the board
    # This first part handles the board building for the Player's Ships
    RowsCount = 1
    WhosShips = ((Gameboard / 2) // 2) + 1
    Row = []
    FullBoard = []
    while RowsCount != (Gameboard / 2) + 1:
        Row.append(format(RowsCount,"<3"))
        for i in range(1,Gameboard + 1):
            Row.append(format(".", "<3"))
        if RowsCount == WhosShips:
            Row.append(format("PLAYER'S SHIPS", "<5"))
        FullBoard.append(Row)
        Row = []
        RowsCount +=1
    # This part handles the board building for the Computer's Ships
    RowsCount2 = 1
    while RowsCount != Gameboard + 1:
        Row.append(format(RowsCount,"<3"))
        for i in range(1,Gameboard+1):
            Row.append(format("*", "<3"))
        if RowsCount2 == WhosShips:
            Row.append(format("COMPUTER'S SHIPS", "<5"))
        FullBoard.append(Row)
        Row = []
        RowsCount +=1
        RowsCount2 += 1
    return FullBoard

def printBoard(Level, FullBoard):
    # This generates the column headig letters for the board
    Gameboard = board(Level)
    LetterCount = 1
    Columns = []
    while LetterCount != Gameboard + 1:
        Columns.append(chr(ord('@') + LetterCount))
        LetterCount += 1
    BoardCols = "    "
    while len(Columns) > 0:
        BoardCols += format(Columns[0],"<4")
        del Columns[0]
    # Display the board through printing 
    PrintRow = ""
    PrintCount = 1
    BoardBreak = (Gameboard / 2) + 1
    print(BoardCols)
    for i in FullBoard:
        for l in i:
            PrintRow += format(l,"<4")
        print(PrintRow)
        PrintCount += 1
        if PrintCount == BoardBreak:
            print("-" * Gameboard * 4 + "--")
        PrintRow = ""

# All ship placement functions are structured the same. See placeBattleship
# function for more code explanation in comments.
def placeAC(Level, FullBoard):
    AircraftCarrier = "Pick a single starting point to place your " \
                      + "Aircraft Carrier - 5? \n(Ex: 'A2' - CASE SENSITIVE): "
    Place1 = 100
    Place2 = 100
    # Handle placement checking - entire ship must be on board
    while Place1 not in range(1,len(FullBoard)) and Place2 not \
          in range(0,len(FullBoard)):
        WhatShip = input(AircraftCarrier)
        try:
            if len(WhatShip) == 2:
                Place1 = int(ord(WhatShip[0])-64)
                Place2 = int(WhatShip[1]) - 1
            elif len(WhatShip) == 3:
                Place1 = int(ord(WhatShip[0])-64)
                WhatShip = WhatShip[1:3]
                Place2 = int(WhatShip) - 1
        except:
            Place1 = 100
            Place2 = 100
        HVCan = ["H", "h", "V", "v"]
        HV = input("Place the ship horizontal or vertical? ('H' or 'V'): ")
        while HV not in HVCan:
            HV = input("Place the ship horizontal or vertical? ('H' or 'V'): ")
        if Place1 > len(FullBoard):
            print("\nPLACEMENT IS OUTSIDE OF YOUR PORTION OF THE BOARD!")
            Place1 = 100
            Place2 = 100
        elif HV == "H" and Place1 + 4 > len(FullBoard) or HV == "h" and \
             Place1 + 4 > len(FullBoard):
            print("\nPLACEMENT IS OUTSIDE OF YOUR PORTION OF THE BOARD!")
            Place1 = 100
            Place2 = 100
        elif Place2 > (len(FullBoard) / 2) - 1:
            print("\nPLACEMENT IS OUTSIDE OF YOUR PORTION OF THE BOARD!")
            Place1 = 100
            Place2 = 100
        elif HV == "V" and Place2 + 4 > (len(FullBoard) / 2) - 1 or HV == "v" \
             and Place2 + 4 > (len(FullBoard) / 2) - 1:
            print("\nPLACEMENT IS OUTSIDE OF YOUR PORTION OF THE BOARD!")
            Place1 = 100
            Place2 = 100
    # This part actually places the ship in the appropriate places
    ACLocation = []
    Count = 0
    if HV == "H" or HV == "h":
        while Count <= 4:
            List = FullBoard[Place2]
            del List[Place1]
            List.insert(Place1,"A")
            del FullBoard[Place2]
            FullBoard.insert(Place2,List)
            ACLocation.append([Place2,Place1])
            Place1 += 1
            Count += 1
    else:
         while Count <= 4:
            List = FullBoard[Place2]
            del List[Place1]
            List.insert(Place1,"A")
            del FullBoard[Place2]
            FullBoard.insert(Place2,List)
            ACLocation.append([Place2,Place1])
            Place2 += 1
            Count += 1
    printBoard(Level, FullBoard)
    return ACLocation

def placeBattleship(Level, FullBoard):
    Battleship = "Pick a single starting point to place your " \
                      + "Battleship - 4? \n(Ex: 'A2' - CASE SENSITIVE): "
    Place1 = 100
    Place2 = 100
    # Handle placement checking - entire ship must be on board
    # The user is to input a single point on the board as the starting point
    # for the ship being placed. In this, Place1 is the column and Place2 is
    # the row - Ex: for A2, Place 1 = A and Place2 = 2.
    while Place1 not in range(1,len(FullBoard)) and Place2 not \
          in range(0,len(FullBoard)):
        WhatShip = input(Battleship)
    # Location must be in format coumn (letter) then row (number). Error check
    # for an instance where the user inputs something not in that format.
        try:
            # Starting point could be 2 characters long - Ex: A2
            if len(WhatShip) == 2:
                Place1 = int(ord(WhatShip[0])-64)
                Place2 = int(WhatShip[1]) - 1
            # Starting point could be 3 characters long - Ex: A10
            elif len(WhatShip) == 3:
                Place1 = int(ord(WhatShip[0])-64)
                WhatShip = WhatShip[1:3]
                Place2 = int(WhatShip) - 1
        except:
            Place1 = 100
            Place2 = 100
        # After picking the starting point, the user is prompted to enter if
        # they want to place the ship horizontally of vertically - 'H' or 'V'.
        # If horizontal the ship is placed from the starting point (inclusive)
        # to the right the apropriate number of spaces. If vertical the ship is
        # placed from the starting point (inclusive) down the apropriate number
        # of spaces. 
        HVCan = ["H", "h", "V", "v"]
        HV = input("Place the ship horizontal or vertical? ('H' or 'V'): ")
        while HV not in HVCan:
            HV = input("Place the ship horizontal or vertical? ('H' or 'V'): ")
        # The ship cannot be placed outside of the player's side of the board.
        WorkingList = []
        try:
            if HV == "H" or HV == "h":
                WorkingList = FullBoard[Place2]
            elif HV == "V" or HV == "v":
                for i in FullBoard:
                   WorkingList.append(i[Place1])
        except:
            Place1 = 100
            Place2 = 100
        # Checks that the starting point is not off the right side of the board.
        if Place1 > len(FullBoard):
            print("\nPLACEMENT IS OUTSIDE OF YOUR PORTION OF THE BOARD!")
            Place1 = 100
            Place2 = 100
        # Checks that the ending point of the ship os not off the right side of
        # the board.
        elif HV == "H" and Place1 + 3 > len(FullBoard) or HV == "h" and \
             Place1 + 3 > len(FullBoard):
            print("\nPLACEMENT IS OUTSIDE OF YOUR PORTION OF THE BOARD!")
            Place1 = 100
            Place2 = 100
        # Checks that the starting point is not off the player's side if the
        # board and into the bottom portion into the computer's side.
        elif Place2 > (len(FullBoard) / 2) - 1:
            print("\nPLACEMENT IS OUTSIDE OF YOUR PORTION OF THE BOARD!")
            Place1 = 100
            Place2 = 100
        # Checks that the ending point of the ship is not off the player's side
        # of the board and into the bottom portion into the computer's side.
        elif HV == "V" and Place2 + 3 > (len(FullBoard) / 2) - 1 or HV == "v" \
             and Place2 + 3 > (len(FullBoard) / 2) - 1:
            print("\nPLACEMENT IS OUTSIDE OF YOUR PORTION OF THE BOARD!")
            Place1 = 100
            Place2 = 100
        # Ships cannot overlap eachother.
        elif HV == "h" or HV == "H":
            for i in WorkingList[Place1:Place1 + 4]:
                if i == "A":
                    print("\nPLACEMENT OVERLAPS WITH ANOTHER SHIP!\n")
                    Place1 = 100
                    Place2 = 100
                    break
        elif HV == "v" or HV == "V":
            for i in WorkingList[Place2:Place2 + 4]:
                if i == "A":
                    print("\nPLACEMENT OVERLAPS WITH ANOTHER SHIP!\n")
                    Place1 = 100
                    Place2 = 100
                    break
    # The ship placement is then built into the board and the individual
    # placement points for the ship are added to a list to be returned.
    # Placement is structures to place the appropriate letter on the board to
    # represent the ship. To change then length of the ship simply change the
    # duration of the while loop with the Count variable. The while loop deletes
    # the character on the board where the ship is being placed and then
    # inserts the ship's corresponding letter to the board in that location. 
    BattleshipLocation = []
    Count = 0
    if HV == "H" or HV == "h":
        while Count <= 3:
            List = FullBoard[Place2]
            del List[Place1]
            List.insert(Place1,"B")
            del FullBoard[Place2]
            FullBoard.insert(Place2,List)
            BattleshipLocation.append([Place2,Place1])
            Place1 += 1
            Count += 1
    else:
         while Count <= 3:
            List = FullBoard[Place2]
            del List[Place1]
            List.insert(Place1,"B")
            del FullBoard[Place2]
            FullBoard.insert(Place2,List)
            BattleshipLocation.append([Place2,Place1])
            Place2 += 1
            Count += 1
    printBoard(Level, FullBoard)
    return BattleshipLocation

def placeCruiser(Level, FullBoard):
    Cruiser = "Pick a single starting point to place your " \
                      + "Cruiser - 3? \n(Ex: 'A2' - CASE SENSITIVE): "
    Place1 = 100
    Place2 = 100
    # Handle placement checking - entire ship must be on board
    while Place1 not in range(1,len(FullBoard)) and Place2 not \
          in range(0,len(FullBoard)):
        WhatShip = input(Cruiser)
        try:
            if len(WhatShip) == 2:
                Place1 = int(ord(WhatShip[0])-64)
                Place2 = int(WhatShip[1]) - 1
            elif len(WhatShip) == 3:
                Place1 = int(ord(WhatShip[0])-64)
                WhatShip = WhatShip[1:3]
                Place2 = int(WhatShip) - 1
        except:
            Place1 = 100
            Place2 = 100
        HVCan = ["H", "h", "V", "v"]
        HV = input("Place the ship horizontal or vertical? ('H' or 'V'): ")
        while HV not in HVCan:
            HV = input("Place the ship horizontal or vertical? ('H' or 'V'): ")
        WorkingList = []
        try:
            if HV == "H" or HV == "h":
                WorkingList = FullBoard[Place2]
            elif HV == "V" or HV == "v":
                for i in FullBoard:
                   WorkingList.append(i[Place1])
        except:
            Place1 = 100
            Place2 = 100
        if Place1 > len(FullBoard):
            print("\nPLACEMENT IS OUTSIDE OF YOUR PORTION OF THE BOARD!")
            Place1 = 100
            Place2 = 100
        elif HV == "H" and Place1 + 2 > len(FullBoard) or HV == "h" and \
             Place1 + 2 > len(FullBoard):
            print("\nPLACEMENT IS OUTSIDE OF YOUR PORTION OF THE BOARD!")
            Place1 = 100
            Place2 = 100
        elif Place2 > (len(FullBoard) / 2) - 1:
            print("\nPLACEMENT IS OUTSIDE OF YOUR PORTION OF THE BOARD!")
            Place1 = 100
            Place2 = 100
        elif HV == "V" and Place2 + 2 > (len(FullBoard) / 2) - 1 or HV == "v" \
             and Place2 + 2 > (len(FullBoard) / 2) - 1:
            print("\nPLACEMENT IS OUTSIDE OF YOUR PORTION OF THE BOARD!")
            Place1 = 100
            Place2 = 100
        # Handles if the new ship placement overlaps another ship on the board
        elif HV == "h" or HV == "H":
            for i in WorkingList[Place1:Place1 + 3]:
                if i == "A" or i == "B":
                    print("\nPLACEMENT OVERLAPS WITH ANOTHER SHIP!\n")
                    Place1 = 100
                    Place2 = 100
                    break
        elif HV == "v" or HV == "V":
            for i in WorkingList[Place2:Place2 + 3]:
                if i == "A" or i == "B":
                    print("\nPLACEMENT OVERLAPS WITH ANOTHER SHIP!\n")
                    Place1 = 100
                    Place2 = 100
                    break
    CruiserLocation = []
    Count = 0
    if HV == "H" or HV == "h":
        while Count <= 2:
            List = FullBoard[Place2]
            del List[Place1]
            List.insert(Place1,"C")
            del FullBoard[Place2]
            FullBoard.insert(Place2,List)
            CruiserLocation.append([Place2,Place1])
            Place1 += 1
            Count += 1
    else:
         while Count <= 2:
            List = FullBoard[Place2]
            del List[Place1]
            List.insert(Place1,"C")
            del FullBoard[Place2]
            FullBoard.insert(Place2,List)
            CruiserLocation.append([Place2,Place1])
            Place2 += 1
            Count += 1
    printBoard(Level, FullBoard)
    return CruiserLocation

def placeSub(Level, FullBoard):
    Submarine = "Pick a single starting point to place your " \
                      + "Submarine - 3? \n(Ex: 'A2' - CASE SENSITIVE): "
    Place1 = 100
    Place2 = 100
    # Handle placement checking - entire ship must be on board
    while Place1 not in range(1,len(FullBoard)) and Place2 not \
          in range(0,len(FullBoard)):
        WhatShip = input(Submarine)
        try:
            if len(WhatShip) == 2:
                Place1 = int(ord(WhatShip[0])-64)
                Place2 = int(WhatShip[1]) - 1
            elif len(WhatShip) == 3:
                Place1 = int(ord(WhatShip[0])-64)
                WhatShip = WhatShip[1:3]
                Place2 = int(WhatShip) - 1
        except:
            Place1 = 100
            Place2 = 100
        HVCan = ["H", "h", "V", "v"]
        HV = input("Place the ship horizontal or vertical? ('H' or 'V'): ")
        while HV not in HVCan:
            HV = input("Place the ship horizontal or vertical? ('H' or 'V'): ")
        WorkingList = []
        try:
            if HV == "H" or HV == "h":
                WorkingList = FullBoard[Place2]
            elif HV == "V" or HV == "v":
                for i in FullBoard:
                   WorkingList.append(i[Place1])
        except:
            Place1 = 100
            Place2 = 100
        if Place1 > len(FullBoard):
            print("\nPLACEMENT IS OUTSIDE OF YOUR PORTION OF THE BOARD!")
            Place1 = 100
            Place2 = 100
        elif HV == "H" and Place1 + 2 > len(FullBoard) or HV == "h" and \
             Place1 + 2 > len(FullBoard):
            print("\nPLACEMENT IS OUTSIDE OF YOUR PORTION OF THE BOARD!")
            Place1 = 100
            Place2 = 100
        elif Place2 > (len(FullBoard) / 2) - 1:
            print("\nPLACEMENT IS OUTSIDE OF YOUR PORTION OF THE BOARD!")
            Place1 = 100
            Place2 = 100
        elif HV == "V" and Place2 + 2 > (len(FullBoard) / 2) - 1 or HV == "v" \
             and Place2 + 2 > (len(FullBoard) / 2) - 1:
            print("\nPLACEMENT IS OUTSIDE OF YOUR PORTION OF THE BOARD!")
            Place1 = 100
            Place2 = 100
        # Handles if the new ship placement overlaps another ship on the board
        elif HV == "h" or HV == "H":
            for i in WorkingList[Place1:Place1 + 3]:
                if i == "A" or i == "B" or i == "C":
                    print("\nPLACEMENT OVERLAPS WITH ANOTHER SHIP!\n")
                    Place1 = 100
                    Place2 = 100
                    break
        elif HV == "v" or HV == "V":
            for i in WorkingList[Place2:Place2 + 3]:
                if i == "A" or i == "B" or i == "C":
                    print("\nPLACEMENT OVERLAPS WITH ANOTHER SHIP!\n")
                    Place1 = 100
                    Place2 = 100
                    break
    SubLocation = []
    Count = 0
    if HV == "H" or HV == "h":
        while Count <= 2:
            List = FullBoard[Place2]
            del List[Place1]
            List.insert(Place1,"S")
            del FullBoard[Place2]
            FullBoard.insert(Place2,List)
            SubLocation.append([Place2,Place1])
            Place1 += 1
            Count += 1
    else:
         while Count <= 2:
            List = FullBoard[Place2]
            del List[Place1]
            List.insert(Place1,"S")
            del FullBoard[Place2]
            FullBoard.insert(Place2,List)
            SubLocation.append([Place2,Place1])
            Place2 += 1
            Count += 1
    printBoard(Level, FullBoard)
    return SubLocation

def placeDestroyer(Level, FullBoard):
    Destroyer = "Pick a single starting point to place your " \
                      + "Destroyer - 2? \n(Ex: 'A2' - CASE SENSITIVE): "
    Place1 = 100
    Place2 = 100
    # Handle placement checking - entire ship must be on board
    while Place1 not in range(1,len(FullBoard)) and Place2 not \
          in range(0,len(FullBoard)):
        WhatShip = input(Destroyer)
        try:
            if len(WhatShip) == 2:
                Place1 = int(ord(WhatShip[0])-64)
                Place2 = int(WhatShip[1]) - 1
            elif len(WhatShip) == 3:
                Place1 = int(ord(WhatShip[0])-64)
                WhatShip = WhatShip[1:3]
                Place2 = int(WhatShip) - 1
        except:
            Place1 = 100
            Place2 = 100
        HVCan = ["H", "h", "V", "v"]
        HV = input("Place the ship horizontal or vertical? ('H' or 'V'): ")
        while HV not in HVCan:
            HV = input("Place the ship horizontal or vertical? ('H' or 'V'): ")
        WorkingList = []
        try:
            if HV == "H" or HV == "h":
                WorkingList = FullBoard[Place2]
            elif HV == "V" or HV == "v":
                for i in FullBoard:
                   WorkingList.append(i[Place1])
        except:
            Place1 = 100
            Place2 = 100
        if Place1 > len(FullBoard):
            print("\nPLACEMENT IS OUTSIDE OF YOUR PORTION OF THE BOARD!")
            Place1 = 100
            Place2 = 100
        elif HV == "H" and Place1 + 1 > len(FullBoard) or HV == "h" and \
             Place1 + 1 > len(FullBoard):
            print("\nPLACEMENT IS OUTSIDE OF YOUR PORTION OF THE BOARD!")
            Place1 = 100
            Place2 = 100
        elif Place2 > (len(FullBoard) / 2) - 1:
            print("\nPLACEMENT IS OUTSIDE OF YOUR PORTION OF THE BOARD!")
            Place1 = 100
            Place2 = 100
        elif HV == "V" and Place2 + 1 > (len(FullBoard) / 2) - 1 or HV == "v" \
             and Place2 + 1 > (len(FullBoard) / 2) - 1:
            print("\nPLACEMENT IS OUTSIDE OF YOUR PORTION OF THE BOARD!")
            Place1 = 100
            Place2 = 100
        # Handles if the new ship placement overlaps another ship on the board
        elif HV == "h" or HV == "H":
            for i in WorkingList[Place1:Place1 + 2]:
                if i == "A" or i == "B" or i == "C" or i == "S":
                    print("\nPLACEMENT OVERLAPS WITH ANOTHER SHIP!\n")
                    Place1 = 100
                    Place2 = 100
                    break
        elif HV == "v" or HV == "V":
            for i in WorkingList[Place2:Place2 + 2]:
                if i == "A" or i == "B" or i == "C" or i == "S":
                    print("\nPLACEMENT OVERLAPS WITH ANOTHER SHIP!\n")
                    Place1 = 100
                    Place2 = 100
                    break
    DestroyerLocation = []
    Count = 0
    if HV == "H" or HV == "h":
        while Count <= 1:
            List = FullBoard[Place2]
            del List[Place1]
            List.insert(Place1,"D")
            del FullBoard[Place2]
            FullBoard.insert(Place2,List)
            DestroyerLocation.append([Place2,Place1])
            Place1 += 1
            Count += 1
    else:
         while Count <= 1:
            List = FullBoard[Place2]
            del List[Place1]
            List.insert(Place1,"D")
            del FullBoard[Place2]
            FullBoard.insert(Place2,List)
            DestroyerLocation.append([Place2,Place1])
            Place2 += 1
            Count += 1
    printBoard(Level, FullBoard)
    return DestroyerLocation
 
def computerShipPlacement(FullBoard):
    # Place the computer's Aircraft Carrier
    ACPlace1 = 100
    ACPlace2 = 100
    ACHV = random.randint(1,2)
    # Make sure the computer's placement is on the board 
    if ACHV == 1:
        while ACPlace1 + 4 not in range(1, len(FullBoard)):
            ACPlace1 = random.randint(1, len(FullBoard))
            ACPlace2 = random.randint(len(FullBoard)/2, len(FullBoard)-1)
    else:
        while ACPlace2 + 4 not in range(1, len(FullBoard)):
            ACPlace2 = random.randint(len(FullBoard)/2, len(FullBoard)-1)
            ACPlace1 = random.randint(1, len(FullBoard))
    # Build the ship's placement location as a nested list. 
    CompAC = []
    Count = 0
    if ACHV == 1:
        while Count <= 4:
            CompAC.append([ACPlace2,ACPlace1])
            ACPlace1 += 1
            Count += 1
    else:
        while Count <= 4:
            CompAC.append([ACPlace2,ACPlace1])
            ACPlace2 += 1
            Count += 1
    # Place the computer's Battleship
    BPlace1 = 100
    BPlace2 = 100
    BHV = random.randint(1,2) 
    if BHV == 1:
        # Make sure the computer's placement is on the board
        while BPlace1 + 3 not in range(1, len(FullBoard)):
            BPlace1 = random.randint(1, len(FullBoard))
            BPlace2 = random.randint(len(FullBoard)/2, len(FullBoard)-1)
            # Make sure that the ship doesn't run into the Aircraft Carrier
            for i in CompAC:
                if i == [BPlace2, BPlace1] or i == [BPlace2, BPlace1 + 1] or \
                   i == [BPlace2, BPlace1 + 2] or i == [BPlace2, BPlace1 + 3]:
                    BPlace1 = 100
    else:
        # Make sure the computer's placement is on the board
        while BPlace2 + 3 not in range(1, len(FullBoard)):
            BPlace2 = random.randint(len(FullBoard)/2, len(FullBoard)-1)
            BPlace1 = random.randint(1, len(FullBoard))
            # Make sure that the ship doesn't run into the Aircraft Carrier
            for i in CompAC:
                if i == [BPlace2, BPlace1] or i == [BPlace2 + 1, BPlace1] or \
                   i == [BPlace2 + 2, BPlace1] or i == [BPlace2 + 3, BPlace1]:
                    BPlace2 = 100
    CompBattleship = []
    Count = 0
    if BHV == 1:
        while Count <= 3:
            CompBattleship.append([BPlace2,BPlace1])
            BPlace1 += 1
            Count += 1
    else:
        while Count <= 3:
            CompBattleship.append([BPlace2,BPlace1])
            BPlace2 += 1
            Count += 1
# Place the computer's Cruiser
    CPlace1 = 100
    CPlace2 = 100
    CHV = random.randint(1,2) 
    if CHV == 1:
        # Make sure the computer's placement is on the board
        while CPlace1 + 3 not in range(1, len(FullBoard)):
            CPlace1 = random.randint(1, len(FullBoard))
            CPlace2 = random.randint(len(FullBoard)/2, len(FullBoard)-1)
            # Make sure that the ship doesn't run into the Aircraft Carrier
            for i in CompAC:
                if i == [CPlace2, CPlace1] or i == [CPlace2, CPlace1 + 1] or \
                   i == [CPlace2, CPlace1 + 2]:
                    CPlace1 = 100
            # Make sure that the ship doesn't run into the Battleship
            for i in CompBattleship:
                if i == [CPlace2, CPlace1] or i == [CPlace2, CPlace1 + 1] or \
                   i == [CPlace2, CPlace1 + 2]:
                    CPlace1 = 100
    else:
        # Make sure the computer's placement is on the board
        while CPlace2 + 3 not in range(1, len(FullBoard)):
            CPlace2 = random.randint(len(FullBoard)/2, len(FullBoard)-1)
            CPlace1 = random.randint(1, len(FullBoard))
            # Make sure that the ship doesn't run into the Aircraft Carrier
            for i in CompAC:
                if i == [CPlace2, CPlace1] or i == [CPlace2 + 1, CPlace1] or \
                   i == [CPlace2 + 2, CPlace1]:
                    CPlace2 = 100
            # Make sure that the ship doesn't run into the Battleship
            for i in CompBattleship:
                if i == [CPlace2, CPlace1] or i == [CPlace2 + 1, CPlace1] or \
                   i == [CPlace2 + 2, CPlace1]:
                    CPlace2 = 100
    CompCruiser = []
    Count = 0
    if CHV == 1:
        while Count <= 2:
            CompCruiser.append([CPlace2,CPlace1])
            CPlace1 += 1
            Count += 1
    else:
        while Count <= 2:
            CompCruiser.append([CPlace2,CPlace1])
            CPlace2 += 1
            Count += 1
# Place the computer's Submarine
    SPlace1 = 100
    SPlace2 = 100
    SHV = random.randint(1,2) 
    if SHV == 1:
        # Make sure the computer's placement is on the board
        while SPlace1 + 3 not in range(1, len(FullBoard)):
            SPlace1 = random.randint(1, len(FullBoard))
            SPlace2 = random.randint(len(FullBoard)/2, len(FullBoard)-1)
            # Make sure that the ship doesn't run into the Aircraft Carrier
            for i in CompAC:
                if i == [SPlace2, SPlace1] or i == [SPlace2, SPlace1 + 1] or \
                   i == [SPlace2, SPlace1 + 2]:
                    SPlace1 = 100
            # Make sure that the ship doesn't run into the Battleship
            for i in CompBattleship:
                if i == [SPlace2, CPlace1] or i == [SPlace2, SPlace1 + 1] or \
                   i == [SPlace2, SPlace1 + 2]:
                    SPlace1 = 100
            # Make sure that the ship doesn't run into the Cruiser
            for i in CompCruiser:
                if i == [SPlace2, CPlace1] or i == [SPlace2, SPlace1 + 1] or \
                   i == [SPlace2, SPlace1 + 2]:
                    SPlace1 = 100
    else:
        # Make sure the computer's placement is on the board
        while SPlace2 + 3 not in range(1, len(FullBoard)):
            SPlace2 = random.randint(len(FullBoard)/2, len(FullBoard)-1)
            SPlace1 = random.randint(1, len(FullBoard))
            # Make sure that the ship doesn't run into the Aircraft Carrier
            for i in CompAC:
                if i == [SPlace2, SPlace1] or i == [SPlace2 + 1, SPlace1] or \
                   i == [SPlace2 + 2, SPlace1]:
                    SPlace2 = 100
            # Make sure that the ship doesn't run into the Battleship
            for i in CompBattleship:
                if i == [SPlace2, SPlace1] or i == [SPlace2 + 1, SPlace1] or \
                   i == [SPlace2 + 2, SPlace1]:
                    SPlace2 = 100
            # Make sure that the ship doesn't run into the Cruiser
            for i in CompCruiser:
                if i == [SPlace2, SPlace1] or i == [SPlace2 + 1, SPlace1] or \
                   i == [SPlace2 + 2, SPlace1]:
                    SPlace2 = 100
    CompSub = []
    Count = 0
    if SHV == 1:
        while Count <= 2:
            CompSub.append([SPlace2,SPlace1])
            SPlace1 += 1
            Count += 1
    else:
        while Count <= 2:
            CompSub.append([SPlace2,SPlace1])
            SPlace2 += 1
            Count += 1
    # Place the computer's Destroyer
    DPlace1 = 100
    DPlace2 = 100
    DHV = random.randint(1,2) 
    if DHV == 1:
        # Make sure the computer's placement is on the board
        while DPlace1 + 3 not in range(1, len(FullBoard)):
            DPlace1 = random.randint(1, len(FullBoard))
            DPlace2 = random.randint(len(FullBoard)/2, len(FullBoard)-1)
            # Make sure that the ship doesn't run into the Aircraft Carrier
            for i in CompAC:
                if i == [DPlace2, DPlace1] or i == [DPlace2, DPlace1 + 1]:
                    DPlace1 = 100
            # Make sure that the ship doesn't run into the Battleship
            for i in CompBattleship:
                if i == [DPlace2, DPlace1] or i == [DPlace2, DPlace1 + 1]:
                    DPlace1 = 100
            # Make sure that the ship doesn't run into the Cruiser
            for i in CompCruiser:
                if i == [DPlace2, DPlace1] or i == [DPlace2, DPlace1 + 1]:
                    DPlace1 = 100
            # Make sure that the ship doesn't run into the Submarine
            for i in CompSub:
                if i == [DPlace2, DPlace1] or i == [DPlace2, DPlace1 + 1]:
                    DPlace1 = 100
    else:
        # Make sure the computer's placement is on the board
        while DPlace2 + 3 not in range(1, len(FullBoard)):
            DPlace2 = random.randint(len(FullBoard)/2, len(FullBoard)-1)
            DPlace1 = random.randint(1, len(FullBoard))
            # Make sure that the ship doesn't run into the Aircraft Carrier
            for i in CompAC:
                if i == [DPlace2, DPlace1] or i == [DPlace2 + 1, DPlace1]:
                    DPlace2 = 100
            # Make sure that the ship doesn't run into the Battleship
            for i in CompBattleship:
                if i == [DPlace2, DPlace1] or i == [DPlace2 + 1, DPlace1]:
                    SPlace2 = 100
            # Make sure that the ship doesn't run into the Cruiser
            for i in CompCruiser:
                if i == [DPlace2, DPlace1] or i == [DPlace2 + 1, DPlace1]:
                    DPlace2 = 100
            # Make sure that the ship doesn't run into the Submarine
            for i in CompSub:
                if i == [DPlace2, DPlace1] or i == [DPlace2 + 1, DPlace1]:
                    DPlace2 = 100
    CompDestroyer = []
    Count = 0
    if DHV == 1:
        while Count <= 1:
            CompDestroyer.append([DPlace2,DPlace1])
            DPlace1 += 1
            Count += 1
    else:
        while Count <= 1:
            CompDestroyer.append([DPlace2,DPlace1])
            DPlace2 += 1
            Count += 1
            
    return CompAC, CompBattleship, CompCruiser, CompSub, CompDestroyer

def playerGuess(CompShipPlaces, CompShips, FullBoard):
    Guess = "Enter a location to bomb (Ex: A" + str(len(FullBoard)) + \
            ")- CASE SENSITIVE: "
    Place1 = 100
    Place2 = 100
    # Checks the validity of the user input
    while Place1 not in range(1,len(FullBoard)) and Place2 not \
          in range(0,len(FullBoard)):
        Location = input(Guess)
        try:
            if len(Location) == 2:
                Place1 = int(ord(Location[0])-64)
                Place2 = int(Location[1]) - 1
            elif len(Location) == 3:
                Place1 = int(ord(Location[0])-64)
                Location = Location[1:3]
                Place2 = int(Location) - 1
        except:
            Place1 = 100
            Place2 = 200
        # Check that the user is bombing a location on the computer's side of
        # the board. 
        if Place1 > len(FullBoard):
            print("\nLOCATION IS OUT OF RANGE!")
            Place1 = 100
            Place2 = 100
        elif Place2 < (len(FullBoard) / 2):
            print("\nYOU CAN'T BOMB YOURSELF!")
            Place1 = 100
            Place2 = 100
        elif Place2 > len(FullBoard):
            print("\nLOCATION IS OUT OF RANGE!")
            Place1 = 100
            Place2 = 100
        # Make sure that the player isn't trying to bomb a location that has
        # already been bombed. 
        try: 
            WorkingList = FullBoard[Place2]
            if WorkingList[Place1] == "O" or WorkingList[Place1] == "X":
                print("\nLOCATION HAS ALREADY BEEN BOMBED")
                Place1 = 100
                Place2 = 100
        except:
            print("INPUT ERROR")
            Place1 = 100
            Place2 = 100
        # Checks if the bombing location is a hit or miss and changes the board
        # accordingly. 
        Hit = False
        for i in CompShipPlaces:
            for j in i:
                if j[0] == Place2 and j[1] == Place1:
                    WhatShip = i
                    idx = CompShipPlaces.index(i)
                    idx2 = WhatShip.index(j)
                    del WhatShip[idx2]
                    del CompShipPlaces[idx]
                    CompShipPlaces.insert(idx, WhatShip)
                    Hit = True
        try:
            WorkingRow = FullBoard[Place2]
            if Hit == True:
                print("\nYOU HIT THEM!!!")
                del WorkingRow[Place1]
                WorkingRow.insert(Place1, "X")
                del FullBoard[Place2]
                FullBoard.insert(Place2, WorkingRow)
                CompShips -= 1
            else:
                print("\nYOU MISSED!")
                del WorkingRow[Place1]
                WorkingRow.insert(Place1, "O")
                del FullBoard[Place2]
                FullBoard.insert(Place2, WorkingRow)
        except:
            Place1 = 100
            Place2 = 100
    # Determines if the player has sunk any of the computer's ships
    if CompShipPlaces[0] == []:
        print("You have sunk their Aircraft Carrier!")
    if CompShipPlaces[1] == []:
        print("You have sunk their Battleship!")
    if CompShipPlaces[2] == []:
        print("You have sunk their Cruiser!")
    if CompShipPlaces[3] == []:
        print("You have sunk their Submarine!")
    if CompShipPlaces[4] == []:
        print("You have sunk their Destroyer!")
        
    return CompShipPlaces, CompShips, FullBoard

def computerGuess(PlayerShips, FullBoard):
    # Randomly guess a location on the board to bomb
    GuessPlace1 = 100
    GuessPlace2 = 100
    while GuessPlace1 not in range(1, len(FullBoard) + 1):
        GuessPlace1 = random.randint(1, len(FullBoard))
        GuessPlace2 = random.randint(0, (len(FullBoard) / 2) - 1)
        # Check that the bombing location hasn't already been bombed
        WorkingRow = FullBoard[GuessPlace2]
        if WorkingRow[GuessPlace1] == "X" or \
           WorkingRow[GuessPlace1] == "O":
            GuessPlace1 = 100
    # Check if the bombed location is a ship
    if WorkingRow[GuessPlace1] == "A" or \
       WorkingRow[GuessPlace1] == "B" or \
       WorkingRow[GuessPlace1] == "C" or \
       WorkingRow[GuessPlace1] == "S" or \
       WorkingRow[GuessPlace1] == "D":
        print("YOU HAVE BEEN HIT!\n")
        del WorkingRow[GuessPlace1]
        WorkingRow.insert(GuessPlace1, "X")
        del FullBoard[GuessPlace2]
        FullBoard.insert(GuessPlace2, WorkingRow)
        PlayerShips -= 1
    else:
        print("THEY MISSED!\n")
        del WorkingRow[GuessPlace1]
        WorkingRow.insert(GuessPlace1, "O")
        del FullBoard[GuessPlace2]
        FullBoard.insert(GuessPlace2, WorkingRow)
    # Determine if a ship has been sunk
    ACount = 0
    BCount = 0
    CCount = 0
    SCount = 0
    DCount = 0
    for i in FullBoard:
        for j in i:
            if j == "A":
                ACount += 1
            elif j == "B":
                BCount += 1
            elif j == "C":
                CCount += 1
            elif j == "S":
                SCount += 1
            elif j == "D":
                DCount += 1
    if ACount == 0:
        print("Your Aircraft Carrier has been sunk!")
    if BCount == 0:
        print("Your Battleship has been sunk!")
    if CCount == 0:
        print("Your Cruiser has been sunk!")
    if SCount == 0:
        print("Your Submarine has been sunk!")
    if DCount == 0:
        print("Your Destroyer has been sunk!")
    PlayerShips = ACount + BCount + CCount + SCount + DCount 
    return PlayerShips, FullBoard

def main():
    print("\nWelcome to Jonah's version of Battleship!" + \
          "\nFollow the directions on the screen to play the game.\n")
    # Gather the level of difficulty form the user 
    Level = input("Please enter the level of difficulty (possibilities 1-9): ")
    while (not Level.isdigit()) or int(Level) > 9 or int(Level) < 1 :
        Level = input("ERROR: Please enter the level of difficulty (1-9): ")  
    Level = int(Level)
    # Initiate and display the gameboard 
    Gameboard = board(Level)
    FullBoard = displayBoard(Gameboard)
    printBoard(Level, FullBoard)
    # Place the player's ships on the board and track their locations 
    print("You have 5 ships to place, each ship takes up a designated number" \
          + " of spaces:")
    print("Aircraft Carrier - 5, Battleship - 4, Cruiser - 3,\nSubmarine - 3, " \
          + "and Destroyer - 2.")
    print()
    ACLocation = placeAC(Level, FullBoard)
    BattleshipLocation = placeBattleship(Level, FullBoard)
    CruiserLocation = placeCruiser(Level, FullBoard)
    SubLocation = placeSub(Level, FullBoard)
    DestroyerLocation = placeDestroyer(Level, FullBoard)
    print("\nALL SHIPS PLACED!")
    
    # Prints the location of the player's ships for testing purposes.
    # Commented out because this information is of no use to the player. 
##    print("\nLocations in format [Row-1, Column] to later be checked if hit.")
##    print("Aircraft Carrier Location: ", ACLocation)
##    print("Battleship Location: ", BattleshipLocation)
##    print("Cruiser Location: ", CruiserLocation)
##    print("Submarine Location: ", SubLocation)
##    print("Destroyer Location: ", DestroyerLocation)
##    print()
    
    # Allow the compurter to place its ships on the board. 
    CompAC, CompBattleship, CompCruiser, CompSub, CompDestroyer = \
            computerShipPlacement(FullBoard)
    # Shows the locations of the computer's ships for testing purposes.
    # Commented out so the user cannot see the computer's ships locations.
##    print("Computer Ship Locations:")
##    print("Aircraft carrier: ", CompAC)
##    print("Battleship: ", CompBattleship)
##    print("Cruiser: ", CompCruiser)
##    print("Submarine: ", CompSub)
##    print("Destroyer: ", CompDestroyer)
    CompShipPlaces = []
    CompShipPlaces.append(CompAC)
    CompShipPlaces.append(CompBattleship)
    CompShipPlaces.append(CompCruiser)
    CompShipPlaces.append(CompSub)
    CompShipPlaces.append(CompDestroyer)
    # Alternate player and computer gueses until either the player's or
    # computer's ships are all sunk.
    print("\nNow try to sink all of the computer's ships before they sink " \
          + "yours!\n")
    # Ships are initalized at 17 because a single player's ships take up 17
    # spaces on the board. So if your ships have been hit 17 times then they
    # have all been sunk. 
    PlayerShips = 17
    CompShips = 17
    Continue = True
    # Alternate player and computer bombing until either ComputerShips or
    # PlayerShips = 0.
    while Continue == True:
        CompShipPlaces, CompShips, FullBoard = \
                        playerGuess(CompShipPlaces, CompShips, FullBoard)
        if CompShipPlaces == [[],[],[],[],[]]:
            Continue = False
        print("\n")
        PlayerShips, FullBoard = computerGuess(PlayerShips, FullBoard)
        printBoard(Level, FullBoard)
        print("\n")
        if PlayerShips == 0:
            Continue = False
    # Determine the winner
    if CompShipPlaces == [[],[],[],[],[]]:
        print("\n! ! ! ! ! ! YOU WIN ! ! ! ! ! !")
    else:
        print("\nOH NO!!! YOU LOST!!!")

# Run the program
main()
# Allow the user the option to play the game again
Play = input("\nPlay Again? ('Y' or 'N'): ")
while Play == "Y" or Play == "y":
    print("\n\n" + "-" * 70 + "\nNEW GAME\n" + "-" * 70 + "\n")
    main()
    Play = input("\nWould you like to play again? ('Y' or 'N'): ")
print("\n----------------------------- END GAME -----------------------------")
#
##
###
####
#####
################################################################################
