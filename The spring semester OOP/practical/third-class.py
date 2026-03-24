class Empty(Exception):
    pass
class Stack:
    def __init__(self):
        self._data = []
    def is_empty(self):
        return len(self._data) == 0
    def __len__(self):
        return len(self._data)
    def push(self,item):
        self._data.append(item)
    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]
    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()
if __name__ == "__main__":
    s = Stack()
    print(s.is_empty())
    print(len(s))

    s.push(10)
    s.push(20)
    s.push(30)
    print(len(s))
    print(s.top())

    popped_item = s.pop()
    print(popped_item)
    print(len(s))
    print(s.top())

    print("遍历元素，会清空所有元素")
    while not s.is_empty():
        print(s.pop() , end = " ")
    print(s.is_empty())

    try:
        s.pop()
    except Empty as e:
        print(e)
        print("栈为空，无法弹出元素")

def is_valid_parentheses(s:str):
    bracket_map = {')':'(','}':'{',']':'['}
    stack = Stack()
    for char in s:
        if char in bracket_map.values():
            stack.push(char)
        elif char in bracket_map.keys():
            if stack.is_empty() or stack.pop() != bracket_map[char]:
                return False
    return stack.is_empty()
if __name__ == "__main__":
    text = ["()","([]{})","{[()]}","({[)]}","((()))","(()"]

    for case in text:
        print(f"{case} is valid: {is_valid_parentheses(case)}")