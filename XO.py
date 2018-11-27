import sys
import os
boardsize = 9
board = {1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9"}

def Printboard():
    for i in range(1,len(board.keys())+1):
        if int(i %3) == 0:
            sys.stdout.write("|{}|\n".format(board[i]))
            if int(i %3) == 0 and i <9:
                for i in range(0,9):
                    sys.stdout.write("-")
                sys.stdout.write("\n")
        else:
            sys.stdout.write("|{}|".format(board[i]))


def win(curruser):
    if board[1] == board[2] and board[2] == board[3]:#diognal
        return True
    elif board[4] == board[5] and board[5] == board[6]:
        return True
    elif board[7] == board[8] and board[8] == board[9]:
        return True
    elif board[1] == board[4] and board[4] == board[7]:#horizontal
        return True
    elif board[2] == board[5] and board[5] == board[8]:
        return True
    elif board[3] == board[6] and board[6] == board[9]:
        return True
    elif board[1] == board[5] and board[5] == board[9]:
        return True
    elif board[3] == board[5] and board[5] == board[7]:
        return True
    else:
        return False

def movment(index,user):
    while index > 9 or  board[index] == user or not str(board[index]).isdigit() :
        print("wrong Index")
        index = movevalidate()
    board[index] = user

def movevalidate():
    userInput = str(raw_input("Choose index for play "))
    while not userInput.isdigit() or (int(userInput) < 0 or int(userInput)>10):
        userInput = str(raw_input("Wrong Input "))
    return int(userInput)

def main():
    moves = 1
    isGame = moves < 10
    while isGame:
        Printboard()
        curruser = "O" if int(moves % 2) == 0 else "X"
        print("{} is now playing".format(curruser)) 
        move = movevalidate()
        movment(move,curruser)
        moves+=1
        if moves > 9:
            print("no more moves")
            return
        if win(curruser):
            print("{} won the game".format(curruser))
            return
        os.system('clear')


if __name__ == "__main__":
    main()