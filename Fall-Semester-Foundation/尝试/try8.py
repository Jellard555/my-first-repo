#format 格式化字符串
#contacts = ['1','2','3','4','5']
#for num in contacts :
    #print(num)
 #   message = num + "lsjjasl\
  #      asjkal" + num 
   # print(f"dqys:{num},xi:{message}")



#gpa_dict = {"li":4.255,"ja":3.456,"xu":2.956}
#for name,gpa in gpa_dict.items():
 #   message_content = '{name} ndgpaw {gpa:.1f}'.format(name = name,gpa = gpa)
  #  print(message_content)

#定义函数
def calculate_sector_(angle,radius):
    sector = angle / 360 * 3.14 * radius ** 2
    print(f"mianjiwei:{sector}")
    return sector
sector1 = calculate_sector_(160,30)
sector2 = calculate_sector_(60,15)
sector3 = calculate_sector_(30,16)
     