#数据像水流一样经过多个处理单元
def filter_upper(s):
    return s.upper()
def filter_replace(s):
    return s.replace("A","@")
data = "apple"
data1 = filter_upper(data)
print(data1)
data2 = filter_replace(data1)
print(data2)
