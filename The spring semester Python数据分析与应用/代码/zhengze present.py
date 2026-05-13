import re
match = re.search(r'[1-9]\d{5}',"BIT 100081")
if match:
    pass
    #print(match.group(0))

match.group(0)

ls = re.findall(r'[1-9]\d{5}' , 'BIT100081 TSU100840')
print(ls)

