board = []
coordinate = [[]]
block = (((0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)), ((0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)), ((0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)), ((3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)), ((3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)), ((3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)), ((6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)), ((6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)), ((6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)))
stack = [0]

def initBoard():
    for i in range(9):
        board.append([0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0])

def initCoordinate():
    for j in range(9):
        coordinate.append([[9, 9], [9, 9], [9, 9], [9, 9], [9, 9], [9, 9], [9, 9], [9, 9], [9, 9]])

def setNumber(num, x, y):
    board[x][y] = num
    if num == 0:
        coordinate[0].append([x, y])
    else:
        coordinate[0].remove([x, y])
        coordinate[num][locateBlock(x, y)] = [x, y]

def inputNumbers():
    seq = input('please input number sequence:')
    if len(seq) == 81:
        n = 0
        for num in seq:
            x = int(n / 9)
            y = n % 9
            if not foundNumber(int(num), x, y) or num == '0':
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

def locateBlock(x, y):
    for i in range(9):
        if (x, y) in block[i]:
            return i

def searchBlock(num, x, y):
    try_ord = block[locateBlock(x, y)]
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
    if searchBlock(num, x, y) or searchRow(num, x) or searchCol(num, y):
        return 1
    else:
        return 0

def easyfill_BlankBased():
    for [x, y] in coordinate[0]:
    return 0

def easyfill_BlockBased():
    for i in range(1, 10):
        for j in range(9):
            if coordinate[i][j] == [9, 9]:
                n = 0
                for (x, y) in block[j]:
                        n += 1
                        temp = (x, y)
                if n == 1:
                    return 1
    return 0

    left = 0
    while newLeft != left:
        left = newLeft
        while easyfill_BlankBased():
            pass
        while easyfill_BlockBased():
            pass


if __name__ == '__main__':
    main()
