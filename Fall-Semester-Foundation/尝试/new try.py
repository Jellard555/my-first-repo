#file1 =  open("C:\\Users\\Jellard\\Desktop\\纯文本\\poem.txt","r", encoding = "utf-8")
#print(file1.readline())
#print(file1.readline())
#file1.close()



with open("C:\\Users\\Jellard\\Desktop\\纯文本\\test.txt","a",encoding = "utf-8") as f:
    #print(f.read())             #用w只能写文件覆盖的，a是添加文件内容
    f.write("起舞弄清影,\n")
    f.write("何似在人间.")
    