name = input ("what is your name")
age = int(input("and your age"))
import datetime 
current_year = datetime.datetime.now().year
birth_year =  current_year - age
print(f'{birth_year} is the year of your birth')