s = "hello"
print(s.upper())
s = s.upper()
print(s)

num_list = [1,6,5,-4,8,94,8]
print(sorted(num_list))

contacts = {"jxnd":"zg",
            "YYDS":"yongyuan"}
contacts["xm"] = "ll"
contacts["xn"] = "lk"
contacts["gg"] = "good game"
print(len(contacts))  #什么时候在print时len不用加str？
query = input ("qingshuru")
if query in contacts:
    print("nizhaode"  + query + "hanyiruxia:")
    print(contacts[query])
else:
    print("nideciwomenmeiyou")
    print("womyou" + str(len(contacts)) + "tiao")

#for的循环
total = 0
for a in range(1,101):
    total = total + a
print(total)

#while 的用法 注意变量的使用：count与total
print("woshichnegxu")
count = 0
total = 0
user_input = input("qingshurushuji tingzhishuruQ")
while user_input != "Q":
    num = float(user_input)
    total += num
    count += 1
    user_input = input("qingshurushuji tingzhishuruQ")
if count == 0 :
    result = 0
else:
    result = total / count
print(f"nidpjzwei {result}")


#format 格式化字符串
contacts = {'dd' : '1',
            'gg' : '2','bb' : '3','aa' : '4','hh' : '5'}
for num in contacts :
    message = num + '''alsjjasl
        asjkal''' + num + '''665
        aklsjaalk'''
    print(send = (num,message))
