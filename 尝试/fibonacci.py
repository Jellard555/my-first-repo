def fibonacci(n):
    a,b = 0,1
    for _ in range(n):
        print(a,end="")
        a,b =b, a+b
fibonacci(10)


student = ["J",["S",["k","l"],"p","q"],"o","y"]
for i,item in enumerate(student):           #enumerate自带索引数字
    print(i,item)
enu_list = list(enumerate(student))
print(enu_list)
enu_dic = dict(enumerate(student))
print(enu_dic)
#递归（Recursion）是编程中一种函数调用自身的解决问题的方法，
#核心是把一个「大问题」拆解为「和原问题逻辑相同但规模更小的子问题」，
#直到子问题小到可以直接解决（即「基线条件 / 终止条件」）
#再通过子问题的解逐步回推，得到原问题的解。
#递归的本质是：自我调用 + 问题拆解 + 终止条件
def halld(n):
    if n == 0 or n == 1:
        return 1
    return n*halld(n-1)
print(halld(6))