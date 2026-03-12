import random
range_number = range(1,50)
select_number = random.sample(range_number,6)
sorted_select_number = sorted(select_number , reverse = False)
print(f"{sorted_select_number} is your loterry ticket")
# sorted function 默认为升序，在后面加入 reverse = True 是降序
# 选数用sample，choice，randit，uniform这几个方法
#randit 是选取一个整数
#uniform是选取一个浮点数
#sample选取k个随机整数，不重复，不仅限于书记，只要是可以迭代的类型
#choice选取k个随机整数，可以重复，有权重的功能 nums2 = random.choices([1, 2, 3], weights=[3, 1, 1], k=5)