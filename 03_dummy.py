a1 = ' '
a2 = ' '
a3 = ' '
b1 = ' '
b2 = ' '
b3 = ' '
c1 = ' '
c2 = ' '
c3 = ' '

board = []
game_end = False

def print_board():
    boards = f'a |{a1}|{a2}|{a3}|\n'\
             f'b |{b1}|{b2}|{b3}|\n'\
             f'c |{c1}|{c2}|{c3}|\n'\
              '   1 2 3'
    print(boards)

def xboard_list(t):
    global a1,a2,a3,b1,b2,b3,c1,c2,c3,board,xturn,oturn,game_end
    
    if t in board:
        print('Position taken, please try again')
        return

    if t == 'a1':
        a1 = 'x'
    elif t == 'a2':
        a2 = 'x'
    elif t == 'a3':
        a3 = 'x'
    elif t == 'b1':
        b1 = 'x'
    elif t == 'b2':
        b2 = 'x'
    elif t == 'b3':
        b3 = 'x'
    elif t == 'c1':
        c1 = 'x'
    elif t == 'c2':
        c2 = 'x'
    elif t == 'c3':
        c3 = 'x'
    else:
        print('Invalid position, try again')
        return

    board.append(t)
    xturn = False
    oturn = True


def oboard_list(t):
    global a1,a2,a3,b1,b2,b3,c1,c2,c3,board,oturn,xturn,game_end
    
    if t in board:
        print('Position taken, please try again')
        return

    if t == 'a1':
        a1 = 'o'
    elif t == 'a2':
        a2 = 'o'
    elif t == 'a3':
        a3 = 'o'
    elif t == 'b1':
        b1 = 'o'
    elif t == 'b2':
        b2 = 'o'
    elif t == 'b3':
        b3 = 'o'
    elif t == 'c1':
        c1 = 'o'
    elif t == 'c2':
        c2 = 'o'
    elif t == 'c3':
        c3 = 'o'
    else:
        print('Invalid position, try again')
        return

    board.append(t)
    oturn = False
    xturn = True


xturn = True
oturn = False

while game_end == False:
    print_board()

    if xturn:
        t = input("X turn (Enter position): ")
        xboard_list(t)
    elif oturn:
        t = input("O turn (Enter position): ")
        oboard_list(t)

    if (a1==a2==a3=='x' or
        b1==b2==b3=='x' or
        c1==c2==c3=='x' or
        a1==b1==c1=='x' or
        a2==b2==c2=='x' or
        a3==b3==c3=='x' or
        a1==b2==c3=='x' or
        a3==b2==c1=='x'):
        print_board()
        print("WINNERRRR SI X!!!")
        game_end = True

    if (a1==a2==a3=='o' or
        b1==b2==b3=='o' or
        c1==c2==c3=='o' or
        a1==b1==c1=='o' or
        a2==b2==c2=='o' or
        a3==b3==c3=='o' or
        a1==b2==c3=='o' or
        a3==b2==c1=='o'):
        print_board()
        print("IKAW ANG WINNER O!!!")
        game_end = True

    if len(board) == 9 and game_end == False:
        print_board()
        print("Draw!!")
        game_end = True
