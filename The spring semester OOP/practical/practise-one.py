#level 1 one
width = float(input("please enter the width of the room (feet)"))
length = float(input("please enter the length of the room (feet)"))
#float_width = float(width)
#float_length = float(length)
area = length * width
print(f"the area of the room is {area} feet")


#level 2 two unfinished
current_year = input("please write down the year")
#dict_of_zodiac ={2000 : "Dragon" , 2001 : "Snack" , 2002 : "Horse" , 2003 : "Sheep" , 2004 : "Monkey"  
              #   , 2005 : "Rooster"  ,  2006 : "Dog" , 2007 : "Pig" , 2008 : "Rat" ,2009 : "Ox"
               #  , 2000 : "Tiger"  ,  2000 : "Hare"} 
mid_number = int(current_year) - 2000
last_number = mid_number % 12
if last_number == 0 :
     print(f"Dragon")

# three 
current_year = input("please write down the year")
if current_year % 400 == 0:
    if current_year % 100 == 0:
          print(f"{current_year} is not a leap year")
    elif current_year % 4 == 0:
          print(f"{current_year} is a leap year")
    else:
         print(f"{current_year} is not a leap year")
else:
     print(f"{current_year} is not a leap year")


# four  review kkk.py to check the detialed process
temperture_dict = {}
for celsius in range(0,101,10):
     fahrenheit = celsius * 9/5 + 32
     temperture_dict[celsius] = fahrenheit
print(f"temperature conversion table ")
print("-" * 30)
for celsius , fahrenheit in temperture_dict.items():
     print(f"{celsius:<15}{fahrenheit<15}")

#level 3 five  unfinished
first_string = str(input("please enter a word"))
my_list = []
letter = first_string.split()
my_list.append(letter)
if len(first_string) % 2 == 0 :
     print()

# six Is there have better solution?
enter_number = input("please enter")
def check_prime(num):
     if num % 2 == 0 or num %  3 == 0:
          return False
     elif num % 5 == 0 or num % 7 == 0 :
          return False
     else:
          return True
a = check_prime(enter_number)

# seven 注意bool值的使用含义，and逻辑关系，函数的分层校验逻辑
enter_password = input("enter a password")
def check_security(password):
     if len(password) < 8:
          return False
     def check_digit(char):
          if len(char) != 1:
               return False
          ascii_code = ord(char)
          return 48 <= ascii_code <= 57
     def check_upper(char):
          if len(char) != 1:
               return False
          ascii_code = ord(char)
          return 65 <= ascii_code <= 90
     def check_lower(char):
          if len(char) != 1:
               return False
          ascii_code = ord(char)
          return 97 <= ascii_code <= 122
     has_digit = False
     has_lower = False
     has_upper = False
     for char in password:
          if check_digit(char):
               has_digit = True
          if check_upper(char):
               has_upper = True
          if check_lower(char):
               has_lower = True
          if has_digit and has_lower and has_upper:
               break
     return has_digit and has_lower and has_upper

result = check_security(enter_password)
if result == True:
     print(f"{enter_password} is a good password")
else:
     print(f"I think the password {enter_password} is risky")

# eight more detail in nnnn.py
import random
range_number = range(1,50)
select_number = random.sample(range_number,6)
sorted_select_number = sorted(select_number)
print(f"{sorted_select_number} is your loterry ticket")

# night
#This is a job interview question. 
#What is the output of the following code and explain why: 
def f(x,l=[]): 
     for i in range(x): 
          l.append(i*i) 
     print(l) 
f(2) 
f(3,[3,2,1]) 
f(3)

# ten
#Write a Python program that takes no input and produces a copy of its own source code as its only 
#output (this is like a computer virus that can replicate itself).
with open("C:\\Users\\Jellard\\Desktop\\python_word\\大一\\The spring semester OOP\\practical\\practise-one.py" , 'r' , encoding = "utf-8") as file:
     code = file.read()
     print(code)