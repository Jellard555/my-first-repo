number_items = int(input("please enter the total number os items you purchased"))
total_price = int(input("the price in total"))
if number_items < 10:
    last_price = total_price
elif  10 <= number_items <= 19:
    last_price = total_price * (1-0.2)
elif 20 <= number_items <= 30:
    last_price = total_price * (1-0.3)
else:
    last_price = total_price * (1-0.5)
print(f"you should pay finally:{last_price}")