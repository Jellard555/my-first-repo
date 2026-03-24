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
#中缀转后缀算法
def prior(pr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    poList = []
    tokenList = pr.split()
    for token in tokenList:
        if token in "QWERTYUIOPLKJHGFDSAZXCVBNM" or  token in "123456789":
            poList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            top_token = opStack.pop()
            while top_token != '(':
                poList.append(top_token)
                top_token = opStack.pop()
        else:
            while not opStack.isEmpty() and prec[opStack.peek()] >= prec[token]:
                poList.append(opStack.pop())
            opStack.push(token)
    while not opStack.isEmpty():
        poList.append(opStack.pop())
    return " ".join(poList)
print(prior(" 1 + 5 * ( 8 - 5 ) + 1 + 6 "))


def postfixEval(postfixExpr):
    opstack = Stack()
    tokenlist = postfixExpr.split()
    for token in tokenlist:
        if token in "0123456789":
            opstack.push(int(token))
        else:
            oper2 = opstack.pop()
            oper1 = opstack.pop()
            result = doMath(token,oper1,oper2)
            opstack.push(result)
    return opstack.pop()
def doMath(op,op1,op2):
    if op == "+":
        return op1 + op2
    elif op == "/":
        return op1 / op2
    elif op == "*":
        return op1 * op2
    else:
        return op1 - op2
print(postfixEval(" 9 8 9 5 3 4 8 6 1 + / * - + * + /"))