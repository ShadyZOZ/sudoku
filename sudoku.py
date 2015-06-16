board = []
coordinate = [[]]
box = (((0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)), ((0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)), ((0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)), ((3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)), ((3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)), ((3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)), ((6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)), ((6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)), ((6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)))

def initBoard():
    for i in range(9):
        board.append([0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0])

def initCoordinate():
    for j in range(9):
        coordinate.append([[9, 9], [9, 9], [9, 9], [9, 9], [9, 9], [9, 9], [9, 9], [9, 9], [9, 9]])
    coordinate.append([])

def fill(num, x, y):
    board[x][y] = num
    if num == 0:
        coordinate[0].append([x, y])
    else:
        coordinate[10].append([x, y])
        coordinate[num][locateBox(x, y)] = [x, y]

def inputNumbers():
    seq = input('please input number sequence:')
    if len(seq) == 81:
        n = 0
        for num in seq:
            x = int(n / 9)
            y = n % 9
            if not foundNumber(int(num), x, y) or num == '0':
                fill(int(num), x, y)
                n += 1
            else:
                return 0
        return 1
    else:
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
    for i in range(9):
        if (x, y) in box[i]:
            return i

def searchBox(num, x, y):
    try_ord = box[locateBox(x, y)]
    for [x, y] in try_ord:
        if board[x][y] == num:
            return 1
    return 0

def searchRow(num, x):
    for i in range(9):
        if board[x][i] == num:
            return 1
    return 0

def searchCol(num, y):
    for i in range(9):
        if board[i][y] == num:
            return 1
    return 0

def foundNumber(num, x, y):
    if searchBox(num, x, y) or searchRow(num, x) or searchCol(num, y):
        return 1
    else:
        return 0

def easyfill():
    for [x, y] in coordinate[0]:
        if [x, y] not in coordinate[10]:
            n = 0
            for i in range(1, 10):
                if not foundNumber(i, x, y):
                    n += 1
                    temp = i
            if n == 1:
                fill(temp, x, y)
                return 1

initBoard()
initCoordinate()
if inputNumbers():
    outputBoard()
else:
    print('please input the right number sequence')
while easyfill():
    pass
outputBoard()
