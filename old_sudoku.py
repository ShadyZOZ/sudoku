a = [[0 for col in range(9)] for row in range(9)]
num = [0 for x in range(10)]
flag = 0
count = 0

def checklegal(i, j):
	global num, a, flag
	flag = 0
	if a[i][j] < 0 or a[i][j] > 9:
		flag = 1
	elif a[i][j] != 0 and num[a[i][j]] != 0:
		for item in num[a[i][j]]:
			if i == item[0] or j == item[1]:
				flag = 1
				break

def checknumber(number, i, j):
	global num, flag
	flag = 1
	for item in num[number]:
		if i == item[0] or j == item[1]:
			flag = 0
			break

def getblocknum(x, y):
	if x < 3:
		if y < 3:
			return 0
		elif y > 5:
			return 2
		else:
			return 1
	elif x > 5:
		if y < 3:
			return 6
		elif y > 5:
			return 8
		else:
			return 7
	else:
		if y < 3:
			return 3
		elif y > 5:
			return 5
		else:
			return 4

def searchnum(number, blocknum):
	global a, flag
	flag = 1
	if blocknum == 0:
		for i in range(0, 3):
			for j in range(0, 3):
				if a[i][j] == number:
					flag = 0
	elif blocknum == 1:
		for i in range(0, 3):
			for j in range(3, 6):
				if a[i][j] == number:
					flag = 0
	elif blocknum == 2:
		for i in range(0, 3):
			for j in range(6, 9):
				if a[i][j] == number:
					flag = 0
	elif blocknum == 3:
		for i in range(3, 6):
			for j in range(0, 3):
				if a[i][j] == number:
					flag = 0
	elif blocknum == 4:
		for i in range(3, 6):
			for j in range(3, 6):
				if a[i][j] == number:
					flag = 0
	elif blocknum == 5:
		for i in range(3, 6):
			for j in range(6, 9):
				if a[i][j] == number:
					flag = 0
	elif blocknum == 6:
		for i in range(6, 9):
			for j in range(0, 3):
				if a[i][j] == number:
					flag = 0
	elif blocknum == 7:
		for i in range(6, 9):
			for j in range(3, 6):
				if a[i][j] == number:
					flag = 0
	elif blocknum == 8:
		for i in range(6, 9):
			for j in range(6, 9):
				if a[i][j] == number:
					flag = 0

def easyfill():
    global num, a
    for blocknum in range(0, 9):
        for number in range(1, 10):
            if num[number] != 0:
                searchnum(number, blocknum)
                if flag:
                    count = 0
                    k = -1
                    for j in num[0]:
                        x = j[0]
                        y = j[1]
                        k = k + 1
                        if getblocknum(x, y) == blocknum:
                            checknumber(number, x, y)
                            if flag:
                                m = x
                                n = y
                                l = k
                                count = count + 1
                    if count == 1:
                        del num[0][l]
                        a[m][n] = number
                        num[number].append([m, n])

def horizontalfill():
	global a, flag, num
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	for i in range(0, 9):
		for j in range(0, 9):
			if a[i][j] != 0:
				for k in range(0, len(b)):
					if b[k] == a[i][j]:
						del b[k]
						break
				break
		if len(b) == 1:
			number = b[0]
			l = -1
			for item in num[0]:
				l = l + 1
				if item == [i, j]:
					break
			del num[0][l]
			a[i][j] = number
			num[number].append([i, j])
		else:
			for n in range(0, len(b)):
				number = b[n]
				if num[number] == 0:
					num[number] = [[i, 9]]
				else:
					num[number].append([i, 9])

def verticalfill():
	global a, flag, num
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	for i in range(0, 9):
		for j in range(0, 9):
			if a[j][i] != 0:
				for k in range(0, len(b)):
					if b[k] == a[j][i]:
						del b[k]
						break
		if len(b) == 1:
			number = b[0]
			l = -1
			for item in num[0]:
				l = l + 1
				if item == [j, i]:
					break
			del num[0][l]
			a[j][i] = number
			num[number].append([j, i])
		else:
			for n in range(0, len(b)):
				number = b[n]
				if num[number] == 0:
					num[number] = [[9, i]]
				else:
					num[number].append([9, i])

# output
def output():
	global a, num
	print("a is:")
	for i in range(0, 9):
		for j in range(0, 9):
			if j == 2 or j == 5:
				print(a[i][j], end = '|')
			else:
				print(a[i][j], end = ' ')
		if i == 2 or i == 5:
			print()
			print('------------------')
		else:
			print()
	print(len(num[0]))

# input
print("input a")
for i in range(0, 9):
	for j in range(0, 9):
		a[i][j] = int(input())
		checklegal(i, j)
		while a[i][j] < 0 or a[i][j] > 9 or flag:
			a[i][j] = int(input("illegal number input, please check again\n"))
			checklegal(i, j)
		if num[a[i][j]] == 0:
			num[a[i][j]] = [[i,j]]
		else:
			num[a[i][j]].append([i,j])
output()

lastleft = len(num[0])
nowleft = lastleft
easyfill()
while lastleft == nowleft:
	lastleft = len(num[0])
	easyfill()
	nowleft = len(num[0])
	output()

horizontalfill()
verticalfill()
output()
	# run = run + 1
for i in range(1, 10):
	if num[i] != 0:
		print(i, ":", 9 - len(num[i]))
	else:
		print(i, ":", 9)
# for j in range(0, 10):
# 	print(j)
# 	print(num[j])
