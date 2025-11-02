def main():
    # x is the main gameloop counter, goes up to 9
    x:int = 0

# should probably introduce some type of validation to ensure that a player cannot pick a number the other player already chose 
# probably save the value each player chooses in a list, then after the if statement in playerSwitcher have and if check if the value 
# is already in the other player's list 

    p1_choices = []
    p2_choices = []

    def playerSwitcher(counter):
        if counter % 2 == 0:
            try:
                p1_input = int(input('Player 1 make your move:'))
            except ValueError:
                print('That is not a valid move, try again!')
            if p1_input < 0 or p1_input > 8 or p1_input in p2_choices or p1_input in p1_choices:
                print('That is not a valid move, try again!')
                playerSwitcher(x)
            else:
                p1_choices.append(p1_input)
                return p1_input
        else:
            try:
                p2_input = int(input('Player 2 make your move:'))
            except ValueError:
                print('That is not a valid move, try again!')
            if p2_input < 0 or p2_input > 8 or p2_input in p1_choices or p2_input in p2_choices:
                print('That is not a valid move, try again!')
                playerSwitcher(x)
            else:
                p2_choices.append(p2_input)
                return p2_input
            


#game_board stores the different positions a player can choose throughout the game
    game_board = [0,1,2,3,4,5,6,7,8]

    winCondition = False

    def winConditionChecker():
        win = False
        winConditions = [
            [0,1,2], [3,4,5], [6,7,8], #Horizontal winConditions
            [0,3,6], [1,4,7], [2,5,8], #Vertical winConditions
            [0,4,8], [2,4,6] #Diagonal winConditions
        ]

        for i in winConditions:
                if i[0] in p1_choices and i[1] in p1_choices and i[2] in p1_choices:
                    win = True
                elif i[0] in p2_choices and i[1] in p2_choices and i[2] in p2_choices:
                    win = True            
        return win
    
    print("\n",
        game_board[0], " - ", game_board[1], " - ", game_board[2], "\n", 
        game_board[3], " - ", game_board[4], " - ", game_board[5], "\n",
        game_board[6], " - ", game_board[7], " - ", game_board[8], "\n" 
        )

    while x < 9 and winCondition == False:
        playerSwitcher(x)
        print("P1: ", p1_choices, "P2: ", p2_choices)    
        0
        winCondition = winConditionChecker()

        for i in p1_choices:
            if i in game_board:
                game_board[i] = 'X'
        for n in p2_choices:
            if n in game_board:
                game_board[n] = 'Y'

        print("\n",
        game_board[0], " - ", game_board[1], " - ", game_board[2], "\n", 
        game_board[3], " - ", game_board[4], " - ", game_board[5], "\n",
        game_board[6], " - ", game_board[7], " - ", game_board[8], "\n" 
        )              
    
        

        def whoWon():
            winConditions = [
            [0,1,2], [3,4,5], [6,7,8], #Horizontal winConditions
            [0,3,6], [1,4,7], [2,5,8], #Vertical winConditions
            [0,4,8], [2,4,6] #Diagonal winConditions
        ]
            for i in winConditions:
                    if i[0] in p1_choices and i[1] in p1_choices and i[2] in p1_choices:
                        return 'Player 1 wins!'
                    elif i[0] in p2_choices and i[1] in p2_choices and i[2] in p2_choices:
                        return 'Player 2 wins!'
                    


        x += 1

        if whoWon() == None:
            None
        else:
            print(whoWon())    

    return("GAME OVER!")

print(main())