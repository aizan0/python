board = [' ' for x in range(10)]#this function is using for user input

def insertLetter(letter,pos):# function parameter one is user other is for his position
    board[pos] = letter

def SpaceIsFree(pos):
    return board[pos] == " "


def printboard(board):
    print("   |   |   ")
    print(' ' + board[1] + ' |  ' + board[2] +  '|' + board[3])
    print("   |   |   ")
    print('-----------')
    print("   |   |   ")
    print(' ' + board[4] + ' |  ' + board[5] + '|' + board[6])
    print("   |   |   ")
    print('-----------')
    print("   |   |   ")
    print(' ' + board[7] + ' |  ' + board[8] + '|' + board[9])
    print("   |   |   ")
    print('-----------')

def isBoardfull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def isWinner(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))

def playerMove():
    run = True
    while run:
        move = input("please select a position to enter the X between 1 to 9")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if SpaceIsFree(move):
                    run = False
                    insertLetter('X' , move)
                else:
                    print('Sorry, this space is occupied')
            else:
                print('please type a number between 1 and 9')
        except:
            print('please type a letter')

def ComputerMove():
    PossibleMoves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0 ]
    move = 0

    for let in ['O' , 'X']:
        for i in PossibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if isWinner(boardcopy, let):
                move = i
                return move

    CornerOpen = []
    for i in PossibleMoves:
        if i in [1 , 3 , 7 , 9]:
            CornerOpen.append(i)

    if len(CornerOpen) > 0:
        move = selectRandom(CornerOpen)
        return move
    if 5 in PossibleMoves:


        move = 5
        return move


    edgesOpen = []
    for i in PossibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def main():
    print("welcome to the game!")
    printboard(board)

    while not(isBoardfull(board)):
        if not(isWinner(board , 'O')):
            playerMove()
            printboard(board)
        else:
            print("sorry you loose")
            break

        if not(isWinner(board , 'X') or isBoardfull(board)):
            move = ComputerMove()
            if move == 0:
                print (" ")
            else:
                insertLetter('O' , move)
                print('Computer placed an o on position' , move , ':')
                printboard(board)

        else:
            print("you win")
            break

    if isBoardfull(board):
        print("Tie Game")



while True:
    x = input("Do you want to play again? y/n")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print("------------------")
        main()
    else:
        break
