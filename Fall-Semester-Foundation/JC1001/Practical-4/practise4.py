input_num = input("please enter a set of positive number(use space to seperate them)")
input_str_mun = input_num.split()
input_int = map(int,input_str_mun)
max_num = max(input_int)
number = int(input('then enter another number'))
if number == 0:
   print("the sequence is over")
elif number > max_num:
    print(f"the large one is {number}")
else:
     print(f"the large one is {max_num}")