import random 
value = input("ues space to seperate")
str_value = value.split()
m = int(str_value[0])
n = int(str_value[1])
k = int(str_value[2])
current_seed = n
for _ in range(m):
    random.seed(current_seed)
    start = 10**(k-1)
    end = 10**k-1
    code = random.randint(start,end)
    print(code)
    current_seed = code

import random
m,n,k=map(int,input().split())
current_seed=n
for _ in range(m):
    random.seed(current_seed)
    num=random.randint(10**(k-1),10**k-1)
    print(f"{num:0{k}d}")
    current_seed=num