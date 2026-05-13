class CountDown:
    last = 0
    def __init__(self,num:int):
        self.last = num + 1
    def __iter__(self):
        return self
    def __next__(self):
        self.last -= 1
        if self.last <= 0 :
            raise StopIteration
        return self.last
    
cd = CountDown(4)
for x in cd:
    print(x)

class PowerTwo:
    def __init__(self,num):
        self.last = num + 1
    def __iter__(self):
        return self
    def __next__(self):
        self.last -= 1
        self.power = 2 ** self.last
        if self.last < 0:
            raise StopIteration
        return self.power   
    
tw = PowerTwo(5)
l = list(tw)
print(l)