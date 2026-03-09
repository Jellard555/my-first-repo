keys = ['a','b']
vals = [10,20]
merged = {k:v for k,v in
zip(keys,vals)}
print(merged)
new = {k.upper(): v**2 for k ,v
in merged.items()}
print(new)

aliens = []
for alien_number in range(30):
    new_alien = {'color':'green','point':5,'speed':'slow'}
    aliens.append(new_alien)
for aliens in aliens[0:5]:
    print(aliens)



def fac(n):
    if n==0:
        return 1
    else:
        return n*fac(n-1)  #return 可以表达交出结果，也可以表明终止计算
print(fac(5))
    