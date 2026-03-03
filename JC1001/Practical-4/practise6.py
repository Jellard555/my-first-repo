caro = 0
caro_list = [minutes for minutes in range(10,31,5)]
burns = []
for minute in caro_list:
    every_burns = minute * 9.7
    burns.append(every_burns)
print(f'{burns} every statistic is relate to every five minutes from 10 to 30')

burns_in_minutes = 9.7
for minutess in range(10,31,5):
    caros = minutess * burns_in_minutes
    print(caros)