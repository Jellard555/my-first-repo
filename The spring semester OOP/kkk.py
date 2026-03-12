temperture_dict = {}
for celsius in range(0,101,10):
     fahrenheit = celsius * 9/5 + 32
     temperture_dict[celsius] = fahrenheit
#出现这种情况的话，如果我只想要最后的结果呢？
#print(temperture_dict)
#如果我想要的是表格的形式呢？不导入任何的库
#打印表头
print(f"Celsius(°C)     Fahrenheit(°C)")
print(30*"-")
for celsius , fahrenheit in temperture_dict.items():
     print(f"{celsius}      {fahrenheit}")
#这样输出的结果存在上下数据不对称的情况，有没有语法可以做到完美的空格？
#存在对齐和宽度控制符 格式：{变量名:<数字}  <>分别为左右对齐 ^为居中对齐 数字是占用的字符宽度
#对上面的代码进行修改
print(f"{'Celsius(°C)':<15}{'Fahrenheit(°C)':<15}")
print(30 * "-")
for celsius , fahrenheit in temperture_dict.items():
     print(f"{celsius:<15}{fahrenheit:<15}")
#以上就是这个版本的最终形式


