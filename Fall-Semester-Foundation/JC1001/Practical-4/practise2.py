savings = 0
import calendar
year = 2022
days = 366 if calendar.isleap(year) else 365
b = int(days) + 1
for a in range(1,b):
    savings = a + savings
print(f"you have {savings}p")