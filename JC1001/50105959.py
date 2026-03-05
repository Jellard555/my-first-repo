
def stringToNum(num_string):
    str_list = str(num_string)
    int_str_list = str_list.split(",")
    int_list = [int(num) for num in int_str_list]
    return int_list
#a = stringToNum('5,6,7,8,8,9,4')
#print(a)

def n_w_h_input(word,float1,float2):
    str_capital = str(word.upper())
    round_float1 = round(float1,1)
    round_float2 = round(float2,1)
    last_tuple = (str_capital,round_float1,round_float2)
    return last_tuple
#b = n_w_h_input("kelsl",5.26,6.145)
#print(b)

def n_w_h_output(name_string,float3,float4):
     output = f"{name_string}’s weight is {float3} and his/her height is {float4}"
     return output
#c = n_w_h_output("Jack",69.7,1.9)
#print(c)

def calcBMI(weight,height):
    BMI =  weight / height / height * 10000
    round_BMI = round(BMI,1)
    return round_BMI
#d = calcBMI(60,1.7)
#print(d)

def bmiCat(BMI):
    if BMI < 18.5:
        return "Underweight"
    elif 18.5 <= BMI <= 24.9:
        return "Healthy"
    elif 25 <= BMI <= 29.9:
        return "Overweight"
    elif 30 <= BMI <= 39.9:
        return"Obese"
    else:
        return "Severely obese"
#e = bmiCat(25)
#print(e)

def bmiReport(name,weight,height,BMI,catogory):
    info = {name:{"weight":weight , "height":height , "BMI":BMI , "weight category":catogory}}
    return info
#f = bmiReport("Jcak",60,1.7,20.8,"Healthy")
#print(f)

def oddList(integer1,integer2):
    if integer1 % 2 == 1 and integer2 % 2 == 1:
        result = [integer1,integer2]
    elif integer1 % 2 == 0 and integer2 % 2 ==1:
        result = [integer2]
    elif integer1 % 2 == 1 and integer2 % 2 ==0:
        result = [integer1]
    else:
        result = f"there are not odd numbers"
    return result
#g = oddList(3,4)
#print(g)

def reverseString(string):
    if len(string) <= 1:
        return string
    reverse_string = ""
    for word in string:
        reverse_string = word + reverse_string 
    return reverse_string
#h = reverseString("kleop")
#print(h)

def startAndEnd(given_list):
    if given_list[0] == given_list[-1]:
        return True
    else:
        return False
#i = startAndEnd([4,6,4])
#print(i)

def createBoard():
    board = []
    for _ in range(3):
        row = ["_","_","_"]
        board.append(row)
    return board
#j = createBoard()

def displayBoard(board):
    for row in board:
        print(row)
#empty_board = displayBoard(j)

def getMove():
    number = input("please enter a number between 1 to 9")
    int_num = int(number)
    if 0 < int_num <= 9:
         print(int_num)
         return int_num
    
    else:
        return False
#k = getMove()

def intToBoard(square):
    num = square - 1
    row = num // 3
    col = num % 3
    return(row,col)
#l = intToBoard(6)
#print(l)

def insertToBoard(tup,board,value):
    row = tup[0]
    col = tup[1]

    if board[row][col] in ("X","O"):
        return (False,board)
    else:
        if value == True:
            piece = "X"
            board[row][col] = piece
            return (True,board)
        else:
            piece = "O"
            board[row][col] = piece
            return (True,board)
#m = insertToBoard((0,0),j,True)
#print(m)

def checkDraw(board):
    for row in board:
        for item in row:
            if item == "_":
                return False
            else:
                return True
#n = checkDraw(j)
#print(n)

def checkWin(board):
    conditions  = [[(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)],
                   [(0,0),(1,0),(2,0)],[(0,1),(1,1),(2,1)],[(0,2),(1,2),(2,2)]
                   [(0,0),(1,1),(2,2)],[(0,2),(1,1),(2,0)]]
    for win_line in conditions:
        mark1 = board[win_line[0][0]][win_line[0][1]]
        mark2 = board[win_line[1][0]][win_line[1][1]]
        mark3 = board[win_line[2][0]][win_line[2][1]]
        if mark1 != "_" and mark1 == mark2 and mark2 == mark3:
            return True
    return False