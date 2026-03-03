personal_info = {'guoji':'cn','xm':'lll','xb':'nan','nl':6}
thekeyiwant =['guoji','nl']
merged = {}
for k,v in personal_info.items():
    if k in thekeyiwant:
        merged[k] = v
print(merged)

#上下是一样的写法，类似将字典切片（有这种说法吗？）
#注意将列表切片时，其中的【  ： 】内可以有两个数字，起始与结束，其实可以省略，但中间必须要有 ： 隔开


new = {k : personal_info[k] for k in thekeyiwant}
print(new)