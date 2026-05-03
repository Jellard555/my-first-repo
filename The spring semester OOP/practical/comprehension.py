#作用：一行代码转换 / 过滤可迭代对象，比 for 循环更快
#支持：列表、集合、字典推导式input_strings = [x**2 for x in range(10)]
input_strings = [x**2 for x in range(10)]
output_integers = [int(num) for num in input_strings]

output_integers = [int(n) for n in input_strings if len(n)<3]
books = ["1",'2','6']
fantasy_authors = {b.author for b in books if b.genre == "fantasy"}




#from the author file

S = [x**2 for x in range(10)]
V = [2**i for i in range(13)]
M = [x for x in S if x % 2 == 0]

print(S)
print(V)
print(M)

# for loop
# Initialize `numbers`
numbers = range(10)
# Initialize `new_list`
new_list = []

# Add values to `new_list`
for n in numbers:
    if n%2==0:
        new_list.append(n**2)

# Print `new_list`
print(new_list)

# list comprehension
# Create `new_list` 
new_list = [n**2 for n in numbers if n%2==0]

# Print `new_list`
print(new_list)


# Nested List Comprehensions
list_of_list = [[1,2,3],[4,5,6],[7,8]]

# Flatten `list_of_list`
results = [y for x in list_of_list for y in x]
print(results)
