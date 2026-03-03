def calulate_area(lenth,width):
    return lenth*width
lenth_one = int(input("please enter lenth of the first room"))
width_one = int(input("please enter width of the first room"))
lenth_two = int(input("please enter lenth of the second room"))
width_two = int(input("please enter width of the second room"))
f_area = calulate_area(lenth_one,width_one)
s_area = calulate_area(lenth_two,width_two)
if f_area == s_area :
    print("they are same")
else :
    if f_area > s_area:
        print("the first one is larger")
    else :
        print("the second one is larger")
