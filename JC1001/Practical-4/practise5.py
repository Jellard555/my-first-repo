input_day_tem = input("please enter the 7 days temperture(use space to seperate)")
input_str = input_day_tem.split()
tem_int = map(int,input_str)
len_num = len(input_str)
sum_num = sum(tem_int)
average = sum_num/len_num
print(f"the average temperture of the 7 days is {average}")
