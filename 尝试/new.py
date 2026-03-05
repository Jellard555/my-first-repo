#s = " hello world "
#str_s = s.strip()
#print(str_s)
total = 0
for num in range(1,101):
    if num %2 != 0:
        total += num
print(total)

def remove_duplicates(list):
    new_list = []
    for item in list:
        if item not in new_list:
            new_list.append(item)
    return new_list

scores = {"小明":85, "小红":92, "小刚":78, "小丽":95, "小强":88}
avg = sum(scores.values()) / len(scores)
max_score = max(scores.values())
max_name = [name for name,s in scores.items() if s == max_score][0]
lower_eighty = [name for name,s in scores.items() if s < 80]

s = input("shuruyigezifu")
upper_count = 0
lower_count = 0
digit_count = 0
for char in s:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
    elif char.isdigit():
        digit_count += 1