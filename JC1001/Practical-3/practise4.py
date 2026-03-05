def cala():
    len = int(input("chang"))
    wid = int(input("kuan"))
    return len*wid

area1 = cala()
area2 = cala()
if area1 == area2 :
    print("they are same")
else :
    if area1 > area2:
        print("the first one is larger")
    else :
        print("the second one is larger")
