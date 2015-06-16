board = []
coordinate = []

def initBoard():
    for i in range(9):
        board.append([0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0])

def initCoordinate():
    base = []
    for i in range(9):
        base.append([9, 9])
    for j in range(10):
        coordinate.append(base)

def inputNumbers():
    seq = input('please input number sequence:')
    if len(seq) == 81:
        n = 0
        for num in seq:
            board[int(n / 9)][n % 9] = int(num)
            n += 1
        return 1
    else:
        print('please input the right number sequence')
        return 0

def outputBoard():
    print('=================')
    print('     result      ')
    print('=================')
    for i in range(9):
        row = []
        for j in range(9):
            row.append(str(board[i][j]))
            if j == 2 or j == 5:
                row.append('|')
            else:
                row.append(' ')
        print(''.join(row))
        if i % 3 == 2:
            print('-----------------')

def locateBox(x, y):
    pass

def searchBox():
    pass

def searchRow():
    pass

def searchCol():
    pass

if inputNumbers():
    outputBoard()
