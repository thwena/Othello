#Jonathan Swena
#Game of Othello
import random
import time
print('\033[1;33;40m')#sets the color of board
def printrules(): #function displays rules, then calls the instructions
    print("Official Rules")
    print("1. Black always moves first.")
    print("2. If on your turn you cannot outflank and flip at least one opposing disc, \nyour turn is forfeited and your opponent moves again. However, if a move \nis available to you, you may not forfeit your turn.")
    print("3. Adisc may outflank any number of discs in one or more rows in any number \nof directions at the same time—horizontally, vertically or diagonally. \n(A row is defined as one or more discs in a con-tinuous straight line.).")
    print("4. You may not skip over your own color disc to out-flank an opposing disc.")
    print("5. Disc(s) mayonly be out-flanked as a direct result of a move and mustfall \nin the direct line of the disc placed down.")
    print("6. All discs outflanked in any one move must be flipped, even if it is to \nthe player's advantage not to flip them at all ")
    print("7. A player whoflips a disc which should not have been turned may correct \nthe mistake as long as the opponent has not made a subsequent move. \nIf the opponent has already moved, \nit is too late to change and the disc(s) remain as IS. ")
    print("8. Once a disc is placed on a square, it can never be moved to another \nsquare later in the game. ")
    print("9. If a player runs out of discs, but still has an opportunity to outflank \nan opposing disc on his or her turn, the opponent must give the player \na disc to use. (This can happen as many times as the player needs and can use a disc.) ")
    print("10. When it is no longer possible for either player to move, the gameis over \nDiscs are counted and the player with the majority of his or her color \ndiscs on the board is the winner. NOTE: It is possible for a game to end \nbefore all 64 squares are filled. ")
    check = input("\nPress enter when you are ready to play......\n")
def instructions(): #Diplays instructions for the game.
    print("Instructions")
    print("When asked which column you would like your piece to be in.\nRefer to the letters above and below the board.")
    print("When asked which row you would like your piece to be in.\nRefer to the numbers right and left of the board.")
    print("Follow onscreen prompts\nIf you choose to use show available moves they will be displayed as '0'")
    check = input("\nPress enter when you are ready to play......\n")
def player1turn(board,show):#Calls all methods and function that has to do with player 1
    
    move = availablemove(board,1)
    if(show):
        showmove(board,1)
    printboard(board)
    if (move):
        choosespot(board,1,show)
    else:
        print("No move available, Player 2 turn")
    if(show):
        resetshowmove()
def player2turn(board,show):#Calls all methods and function that has to do with player 2
    move = availablemove(board,2)
    if(show):
        showmove(board,2)
    printboard(board)
    if (move):
        choosespot(board,2,show)
    else:
        print("No move available, Player 1 turn")
    if(show):
        resetshowmove()
def computerturn(board,show,player,demo,playernum):#Picks a random index then calls methods to check and flip pieces and place pieces
    move = availablemove(board,playernum)
    check = True
    place1=0
    place2=0
    if(player == '\033[1;36;40mB\033[1;33;40m') and demo:
        print("Computer 1")
    if(player == '\033[1;37;40mW\033[1;33;40m') and demo:
        print("Computer 2")
    if(move):
        row = random.randint(0,9)
        col = random.randint(0,9)
        playable = checkloc(board,col,row,player,check,show)
        while(playable != True):
            row = random.randint(0,9)
            col = random.randint(0,9)
            playable = checkloc(board,col,row,player,check,show)
        placeloc(board,col,row,player,)
        check = False
        flippieces(board,col,row,player,check)
        if(demo):
            if(col == 1):
                place1='a'
            elif(col==2):
                place1='b'
            elif(col==3):
                place1='c'
            elif(col==4):
                place1='d'
            elif(col==5):
                place1='e'
            elif(col==6):
                place1='f'
            elif(col==7):
                place1='g'
            elif(col==8):
                place1='h'
            place2 = str(row)
            print(place1," ",place2)
        printboard(board)        
def twoplayergame(board):#Method for playing game with 2 players
    play = True
    show1=False
    show2=False
    flag = 0
    printboard(board)
    showP1 = input("If player 1 would like see available moves please type 'yes' and type 'no' if not\n")
    while((showP1!='yes')or(showP1!='no')):
        if(showP1=='yes'):
            show1=True
            break
        elif(showP1=='no'):
            break
        showP1 = input("If player 1 would like see available moves please type 'yes' and type 'no' if not\n")
    showP2 = input("If player 2 would like see available moves please type 'yes' and type 'no' if not\n")
    while((showP2!='yes')or(showP2!='no')):
        if(showP2=='yes'):
            show2=True
            break
        elif(showP2=='no'):
            break
        showP2 = input("If player 2 would like see available moves please type 'yes' and type 'no' if not\n")
    
    x=input("press enter to play\n")
    while(flag==0):
        player1turn(board,show1)
        player2turn(board,show2)
        play = (availablemove(board,1) or availablemove(board,2))
        if(play!=True):
            flag = 1
    endgame(board)
def oneplayergame(board):#Method for playing game with 1 player, uses computerturn method for second player
    play = True
    show1=False
    show2=False
    flag = 0
    printboard(board)
    showP1 = input("If player 1 would like see available moves please type 'yes' and type 'no' if not\n")
    while((showP1!='yes')or(showP1!='no')):
        if(showP1=='yes'):
            show1=True
            break
        elif(showP1=='no'):
            break
        showP1 = input("If player 1 would like see available moves please type 'yes' and type 'no' if not\n")
    x=input("press enter to play\n")
    show2 = False
    while(flag==0):
        player1turn(board,show1)
        printboard(board)
        print("Computer Turn")
        time.sleep(2.5)
        computerturn(board,show2,'\033[1;37;40mW\033[1;33;40m',False,2)
        play = (availablemove(board,1) or availablemove(board,2))
        if(play!=True):
            flag = 1
    endgame(board)
def demogame(board):#WIll run a demo game, displaying which computer turn it is and the displays where the computer went
    delay = .5 #makes it look like the computer is thinking
    play = True
    show1 = False
    show2 = False
    printboard(board)
    flag = 0
    while(flag==0):
        time.sleep(delay)
        computerturn(board,show1,'\033[1;36;40mB\033[1;33;40m',True,1)
        time.sleep(delay)
        computerturn(board,show2,'\033[1;37;40mW\033[1;33;40m',True,2)
        play = (availablemove(board,1) or availablemove(board,2))
        if(play!=True):
            flag = 1
            break
    endgame(board)
def createboard(): #Creates the default board and calls setboard and print board
    rows, cols = (10,10)
    board = [['0' for i in range(cols)] for j in range(rows)]
    board[0][0] = " "
    board[0][9] = " "
    board[9][9] = " "
    board[9][0] = " "
    for x in range(1,rows-1, 1):
        board[0][x]=x
        board[9][x]=x
    board[1][0] = '\033[1;33;40ma'
    board[2][0] = 'b'
    board[3][0] = 'c'
    board[4][0] = 'd'
    board[5][0] = 'e'
    board[6][0] = 'f'
    board[7][0] = 'g'
    board[8][0] = 'h'
    board[1][9] = 'a'
    board[2][9] = 'b'
    board[3][9] = 'c'
    board[4][9] = 'd'
    board[5][9] = 'e'
    board[6][9] = 'f'
    board[7][9] = 'g'
    board[8][9] = 'h\033[1;32;40m'
    setboard(board)
    return board
def setboard(board): #sets up the initial board, calls clear board at begining
    clearboard(board)
    board[4][4] = '\033[1;37;40mW\033[1;33;40m'
    board[5][5] = '\033[1;37;40mW\033[1;33;40m'
    board[4][5] = '\033[1;36;40mB\033[1;33;40m'
    board[5][4] = '\033[1;36;40mB\033[1;33;40m'
    
    
def clearboard(board):   #Clears any pieces that may be on the board
    for x in range(1, 9,1):
        board[1][x]= '\033[1;32;40m-\033[1;33;40m'
        board[2][x]= '\033[1;32;40m-\033[1;33;40m'
        board[3][x]= '\033[1;32;40m-\033[1;33;40m'
        board[4][x]= '\033[1;32;40m-\033[1;33;40m'
        board[5][x]= '\033[1;32;40m-\033[1;33;40m'
        board[6][x]= '\033[1;32;40m-\033[1;33;40m'
        board[7][x]= '\033[1;32;40m-\033[1;33;40m'
        board[8][x]= '\033[1;32;40m-\033[1;33;40m'
def printboard(board): #Prints the board, calls score and prints the score
    x = 0
    y = 0
    print("\t      OTHELLO")
    for row in board:
        x=0
        print("\t",end='')
        for cols in board:
            print(board[x][y],end=" ")
            x+=1
        print("")
        y+=1
    bpoint,wpoint = score(board)
    print("\n\033[1;36;40mBlack: \033[1;33;40m",bpoint,"\t\033[1;37;40mWhite: \033[1;33;40m",wpoint)
def score(board): #Calculates the score based off the pieces that are on the board
    x = 0
    y = 0
    wpoints = 0
    bpoints = 0
    for row in board:
        x=0
        for cols in board:
            if board[x][y] == '\033[1;37;40mW\033[1;33;40m':
                wpoints+=1
            elif board[x][y] == '\033[1;36;40mB\033[1;33;40m':
                bpoints+=1
            x+=1
        y+=1
    return bpoints,wpoints
def endgame(board): #Takes the score and display which player won
    bpoint,wpoint = score(board)
    print("\n\033[1;36;40mBlack: \033[1;33;40m",bpoint,"\t\033[1;37;40mWhite: \033[1;33;40m",wpoint)
    if (bpoint>wpoint):
        print("Black Won!")
    elif (wpoint>bpoint):
        print("White Won!")
    else:
        print("Tie!")
def availablemove(board,player):#Will check and see if there is an available move for the player given
    check = True
    possible = False
    show = False
    if player == 1:
        player1 = '\033[1;36;40mB\033[1;33;40m'
    elif player == 2:
        player1 = '\033[1;37;40mW\033[1;33;40m'
    for row in range(1,9,1):
        for col in range(1,9,1):
            if (checkloc(board,row,col,player,check,show)):
                possible = True
    return possible
def showmove(board,player):#Displays the available moves for a given player as a '0'
    check = True
    show = False
    if player == 1:
        player1 = '\033[1;36;40mB\033[1;33;40m'
    elif player == 2:
        player1 = '\033[1;37;40mW\033[1;33;40m'
    for row in range(1,9,1):
        for col in range(1,9,1):
            if (checkloc(board,row,col,player,check,show)):
                board[row][col] = '0'
def resetshowmove():#Clears the '0's off the board so that there are no more moves being shown
    for row in range(1,9,1):
        for col in range(1,9,1):
            if (board[row][col]=='0'):
                board[row][col] = '\033[1;32;40m-\033[1;33;40m'
def choosespot(board,player,show):#player must int 1 or int 2, changes the player into usuable format, calls spotloc(),
                             #then call checkloc(), and determines whether move is legal, if illegal ask player again
                             #call placeloc(), flippieces(), and then printboard()
    check = True
    player2 = player
    if player == 1:
        player1 = '\033[1;36;40mB\033[1;33;40m'
    elif player == 2:
        player1 = '\033[1;37;40mW\033[1;33;40m'
    x,y = spotloc(player2)
    playable = checkloc(board,x,y,player1,check,show)
    while (playable != True):
        printboard(board)
        print("Invalid move please enter a valid move")
        x,y = spotloc(player2)
        playable = checkloc(board,x,y,player1,check,show)
    placeloc(board,x,y,player1)
    check = False
    flippieces(board,x,y,player1,check)

def spotloc(player):#asks user where they would like to play, converts user input into usuable format,
              #makes sure they input it correctly, and then returns the location
    flag = 0
    while (flag != 1):
        if player == 1:
            player1 = '\033[1;36;40mB\033[1;33;40m'
            print("\033[1;36;40mPlayer 1\033[1;33;40m\nPlease enter the column where you would like to place your piece: ")
        elif player == 2:
            player1 = '\033[1;37;40mW\033[1;33;40m'
            print("\033[1;37;40mPlayer 2\033[1;33;40m\nPlease enter the column where you would like to place your piece: ")
        x=input()
        if (x=='a'):
            x=1
            flag = 1
            break
        if (x=='b'):
            x=2
            flag = 1
            break
        if (x=='c'):
            x=3
            flag = 1
            break
        if (x=='d'):
            x=4
            flag = 1
            break
        if (x=='e'):
            x=5
            flag = 1
            break
        if (x=='f'):
            x=6
            flag = 1
            break
        if (x=='g'):
            x=7
            flag = 1
            break
        if (x=='h'):
            x=8
            flag = 1
            break
        else:
            print("Error please try again")
    flag = 0
    while (flag != 1):
        print("Please enter the row where you would like to place your piece: ")
        y=input()
        if (y=='1' or
            y=='2' or
            y=='3' or
            y=='4' or
            y=='5' or
            y=='6' or
            y=='7' or
            y=='8'):
            y = int(y)
            flag = 1
            break
        else:
            print("Error please try again")
    return x,y
def checkloc(board,x,y,player,check,show): #calls other methods to check each individual direction,
                                #and then takes the returned information and determines wether it is legal move or not
                                #The letters are related to directions r: Right, l: Left, u: Up, d: Down,
                                #h: Horizontal, v: Vertical; Horizontal means only on the x-axis, Vertical means only on y-axis
    if player == 1:
        player = '\033[1;36;40mB\033[1;33;40m'
    elif player == 2:
       player = '\033[1;37;40mW\033[1;33;40m'
    ru,rux,ruy = checkru(board,x,y,player,check,show)
    rd,rdx,rdy = checkrd(board,x,y,player,check,show)
    lu,lux,luy = checklu(board,x,y,player,check,show)
    ld,ldx,ldy = checkld(board,x,y,player,check,show)
    hl,hlx,hly = checkhl(board,x,y,player,check,show)
    hr,hrx,hry = checkhr(board,x,y,player,check,show)
    vu,vux,vuy = checkvu(board,x,y,player,check,show)
    vd,vdx,vdy = checkvd(board,x,y,player,check,show)
    if ru:
        return True
    if rd==True:
        return True
    if lu==True:
        return True
    if ld==True:
        return True
    if hl==True:
        return True
    if hr==True:
        return True
    if vu==True:
        return True
    if vd==True:
        return True
    else:
        return False
def placeloc(board,x,y,player):#Takes the player and location of where to place the piece and then places it
    board[x][y] = player
def flippieces(board,x,y,player,check):#Flips all the pieces that need to be flipped
    show = False
    ru,rux,ruy = checkru(board,x,y,player,check,show)
    rd,rdx,rdy = checkrd(board,x,y,player,check,show)
    lu,lux,luy = checklu(board,x,y,player,check,show)
    ld,ldx,ldy = checkld(board,x,y,player,check,show)
    hl,hlx,hly = checkhl(board,x,y,player,check,show)
    hr,hrx,hry = checkhr(board,x,y,player,check,show)
    vu,vux,vuy = checkvu(board,x,y,player,check,show)
    vd,vdx,vdy = checkvd(board,x,y,player,check,show)
    if ru:
        y2=y
        for x2 in range(x,rux,1):
            board[x2][y2]=player
            y2-=1     
    if rd:
        y2=y
        for x2 in range(x,rdx,1):
            board[x2][y2]=player
            y2+=1
    if lu:
        y2=y
        for x2 in range(x,lux,-1):
            board[x2][y2]=player
            y2-=1 
    if ld:
        y2=y
        for x2 in range(x,ldx,-1):
            board[x2][y2]=player
            y2+=1   
    if hl:
        for x2 in range(x,hlx,-1):
            board[x2][hry]=player  
    if hr:
        for x2 in range(x,hrx,1):
            board[x2][hry]=player  
    if vu:
        for y2 in range(y,vuy,-1):
            board[vux][y2]=player
    if vd:
        for y2 in range(y,vdy,1):
            board[vdx][y2]=player
        
def checkru(board,x,y,player,check,show):#checks in the specified direction to make
                             #sure it is a legal move and returns true or false accordingly
    if(show!=True):
        if(board[x][y]!='\033[1;32;40m-\033[1;33;40m')and check:
            return False,x,y
    elif(show):
        if(board[x][y]!='0')and check:
            return False,x,y
    x2=x+1
    y2=y-1
    if(board[x2][y2]==player)or(board[x2][y2]=='\033[1;32;40m-\033[1;33;40m')or(x2==9)or(y2==0)or(board[x2][y2]=='0'):
        return False,x2,y2
    for num1 in range(1,7,1):
        if(x2+num1==9)or(y2-num1==0):
            break
        if(board[x2][y2]=='\033[1;32;40m-\033[1;33;40m'):
            break
        if (board[x2+num1][y2-num1]==player):
            x3 = x2+num1
            y3 = y2-num1
            return True,x3,y3
    return False,x2,y2
def checkrd(board,x,y,player,check,show):#checks in the specified direction to make
                             #sure it is a legal move and returns true or false accordingly
    if(show!=True):
        if(board[x][y]!='\033[1;32;40m-\033[1;33;40m')and check:
            return False,x,y
    elif(show):
        if(board[x][y]!='0')and check:
            return False,x,y
    x2=x+1
    y2=y+1
    if(board[x2][y2]==player)or(board[x2][y2]=='\033[1;32;40m-\033[1;33;40m')or(x2==9)or(y2==9)or(board[x2][y2]=='0'):
        return False,x2,y2
    for num1 in range(1,7,1):
        if(x2+num1==9)or(y2+num1==9):
            break
        if(board[x2][y2]=='\033[1;32;40m-\033[1;33;40m'):
            break
        if (board[x2+num1][y2+num1]==player):
            x3 = x2+num1
            y3 = y2+num1
            return True,x3,y3
    return False,x2,y2
def checklu(board,x,y,player,check,show):#checks in the specified direction to make
                             #sure it is a legal move and returns true or false accordingly
    if(show!=True):
        if(board[x][y]!='\033[1;32;40m-\033[1;33;40m')and check:
            return False,x,y
    elif(show):
        if(board[x][y]!='0')and check:
            return False,x,y
    x2=x-1
    y2=y-1
    if(board[x2][y2]==player)or(board[x2][y2]=='\033[1;32;40m-\033[1;33;40m')or(x2==0)or(y2==0)or(board[x2][y2]=='0'):
        return False,x2,y2
    for num1 in range(1,7,1):
        if(x2-num1==0)or(y2-num1==0):
            break
        if(board[x2][y2]=='\033[1;32;40m-\033[1;33;40m'):
            break
        if (board[x2-num1][y2-num1]==player):
            x3 = x2-num1
            y3 = y2-num1
            return True,x3,y3
    return False,x2,y2
def checkld(board,x,y,player,check,show):#checks in the specified direction to make
                             #sure it is a legal move and returns true or false accordingly
    if(show!=True):
        if(board[x][y]!='\033[1;32;40m-\033[1;33;40m')and check:
            return False,x,y
    elif(show):
        if(board[x][y]!='0')and check:
            return False,x,y
    x2=x-1
    y2=y+1
    if(board[x2][y2]==player)or(board[x2][y2]=='\033[1;32;40m-\033[1;33;40m')or(x2==0)or(y2==9)or(board[x2][y2]=='0'):
        return False,x2,y2
    for num1 in range(1,7,1):
        if(x2-num1==0)or(y2+num1==9):
            break
        if(board[x2][y2]=='\033[1;32;40m-\033[1;33;40m'):
            break
        if (board[x2-num1][y2+num1]==player):
            x3 = x2-num1
            y3 = y2+num1
            return True,x3,y3
    return False,x2,y2
def checkhl(board,x,y,player,check,show):#checks in the specified direction to make
                             #sure it is a legal move and returns true or false accordingly
    if(show!=True):
        if(board[x][y]!='\033[1;32;40m-\033[1;33;40m')and check:
            return False,x,y
    elif(show):
        if(board[x][y]!='0')and check:
            return False,x,y
    x2=x-1
    y2=y
    if(board[x2][y2]==player)or(board[x2][y2]=='\033[1;32;40m-\033[1;33;40m')or(x2==0)or(board[x2][y2]=='0'):
        return False,x2,y2
    for num1 in range(1,7,1):
        if(x2-num1==0):
            break
        if(board[x2][y2]=='\033[1;32;40m-\033[1;33;40m'):
            break
        if (board[x2-num1][y2]==player):
            x3 = x2-num1
            y3 = y2
            return True,x3,y3
    return False,x2,y2
def checkhr(board,x,y,player,check,show):#checks in the specified direction to make
                             #sure it is a legal move and returns true or false accordingly
    if(show!=True):
        if(board[x][y]!='\033[1;32;40m-\033[1;33;40m')and check:
            return False,x,y
    elif(show):
        if(board[x][y]!='0')and check:
            return False,x,y
    x2=x+1
    y2=y
    if(board[x2][y2]==player)or(board[x2][y2]=='\033[1;32;40m-\033[1;33;40m')or(x2==9)or(board[x2][y2]=='0'):
        return False,x2,y2
    for num1 in range(1,7,1):
        if(x2+num1==9):
            break
        if(board[x2][y2]=='\033[1;32;40m-\033[1;33;40m'):
            break
        if (board[x2+num1][y2]==player):
            x3 = x2+num1
            y3 = y2
            return True,x3,y3
    return False,x2,y2
def checkvu(board,x,y,player,check,show):#checks in the specified direction to make
                             #sure it is a legal move and returns true or false accordingly
    if(show!=True):
        if(board[x][y]!='\033[1;32;40m-\033[1;33;40m')and check:
            return False,x,y
    elif(show):
        if(board[x][y]!='0')and check:
            return False,x,y
    x2=x
    y2=y-1
    if(board[x2][y2]==player)or(board[x2][y2]=='\033[1;32;40m-\033[1;33;40m')or(y2==0)or(board[x2][y2]=='0'):
        return False,x2,y2
    for num1 in range(1,7,1):
        if(y2-num1==0):
            break
        if(board[x2][y2-num1]=='\033[1;32;40m-\033[1;33;40m'):
            break
        if (board[x2][y2-num1]==player):
            x3 = x2
            y3 = y2-num1
            return True,x3,y3
    return False,x2,y2
def checkvd(board,x,y,player,check,show):#checks in the specified direction to make
                             #sure it is a legal move and returns true or false accordingly
    if(show!=True):
        if(board[x][y]!='\033[1;32;40m-\033[1;33;40m')and check:
            return False,x,y
    elif(show):
        if(board[x][y]!='0')and check:
            return False,x,y
    x2=x
    y2=y+1
    if(board[x2][y2]==player)or(board[x2][y2]=='\033[1;32;40m-\033[1;33;40m')or(y2==9)or(board[x2][y2]=='0'):
        return False,x2,y2
    for num1 in range(1,7,1):
        if(y2+num1==9):
            break
        if(board[x2][y2+num1]=='\033[1;32;40m-\033[1;33;40m'):
            break
        if (board[x2][y2+num1]==player):
            x3 = x2
            y3 = y2+num1
            return True,x3,y3
    return False,x2,y2
board = createboard()
print("\tOTHELLO")
answer = input("Would you like to see the rules for Othello?\nanswer with 'yes' or 'no'\n")
while(answer!='yes') or (answer!='no'):
    if(answer=='yes'):
        printrules()
        break
    elif(answer=='no'):
        break
    answer = input("Would you like to see the rules for Othello?\nanswer with 'yes' or 'no'\n")
answer = input("Would you like to see the instructions for this game?\nanswer with 'yes' or 'no'\n")
while(answer!='yes') or (answer!='no'):
    if(answer=='yes'):
        instructions()
        break
    elif(answer=='no'):
        break
    answer = input("Would you like to see the instructions for this game?\nanswer with 'yes' or 'no'\n")

answer = input("If you want 1 player please type: '1'\nIf you would like 2 player please type: '2'\nIf you would like a demo gane please type: '3'\n")
gamemode = 0

while(answer!='1') or (answer!='2'):
    if(answer=='1'):
        gamemode = 1
        break
    elif(answer=='2'):
        gamemode = 2
        break
    elif(answer=='3'):
        gamemode = 3
        break
    answer = input("If you want 1 player please type: '1'\nIf you would like 2 player please type: '2'\nIf you would like a demo gane please type: '3'\n")
if (gamemode == 1):
    oneplayergame(board)
elif(gamemode == 2):
    twoplayergame(board)
elif(gamemode == 3):
    demogame(board)
answer2 = input("If you would like to play again press '1' if not press any other key\n")
while(answer2 == 1):
    while(answer!='1') or (answer!='2'):
        if(answer=='1'):
            gamemode = 1
            break
        elif(answer=='2'):
            gamemode = 2
            break
        elif(answer=='3'):
            gamemode = 3
            break
        answer = input("If you want 1 player please type: '1'\nIf you would like 2 player please type: '2'\nIf you would like a demo gane please type: '3'\n")
    if (gamemode == 1):
        oneplayergame(board)
    elif(gamemode == 2):
        twoplayergame(board)
    elif(gamemode == 3):
        demogame(board)
    answer2 = input("If you would like to play again press '1' if not press any other key\n")



