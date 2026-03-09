aDict ={'Hundred':100,'Ninety':90,'Eighty':80,'Seventy':70,'Sixty':60,}
bDict ={'Fifty':50, 'Forty':40, 'Thirty':30, 'Twenty':20, 'Ten':10}
merged = {k:v for d in [aDict,bDict]  #k v d 是可以随便命名的 字典的合并与列表的合并一致 不过合并时的形式不同 列表用逗号，字典用.items()
for k,v in d.items()}
print(merged)