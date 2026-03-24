class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items) - 1]
    def size(self):
        return len(self.items)
#s = Stack()
#print(s.isEmpty())
#s.push('kkkk')
#s.push(4)
#print(s.pop())

def Match(a,b):
    opens = '([{'
    closes = ')]}'
    return opens.index(a) == closes.index(b) 

def parChecker(symbol):
    s = Stack()
    balance = True
    index = 0
    while index < len(symbol) and balance:
        i = symbol[index]
        if i in '([{':
            s.push(i)
        else:
            if s.isEmpty():
                balance = False
            else:
                top = s.pop()
                if not Match(top,i):
                    balance = False 
        index += 1
    if s.isEmpty() and balance:
        return True
    else:
        return False
#print(parChecker("[[(({{}}))]]"))
def Numpy(decimal):
    remstack = Stack()
    rest = {10: "A",11: "B",12: "C",13: "D",14: "E",15: "F"}
    while decimal > 0:
        rem = decimal % 16
        if rem in rest:
            remstack.push(rest[rem])
        else:
            remstack.push(str(rem))
        decimal = decimal // 16
    binstring = ''
    while not remstack.isEmpty():
        binstring = binstring + str(remstack.pop())
    return binstring
print(Numpy(233)) 