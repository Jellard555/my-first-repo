with open("C:\\Users\\Jellard\\Desktop\\poem.txt","w",encoding = "utf-8" ) as f:
    f.write("我欲乘风飞去，\n" "又恐琼楼玉宇，\n" "高处不胜寒.")
   

file = r"C:\\Users\\Jellard\\Desktop\\test.txt"
try :
    with open(file,'r',encoding = 'utf-8') as f:
        content = f.read()
        print("wjnr",content)
except FileNotFoundError:
    print(f'cuole{file}buzai')


with open('C:\\Users\\Jellard\\Desktop\\shi.txt' , 'r' ,encoding ='utf-8') as f:
    print(f.readline())
    print(f.readline()) 
    


#try and except 是用来防止因用户输入问题而产生的错误
#try后面放可能出现错误的程序
#except后面放错误类型 可以多几个except
#如果except后面不加任何种类的错误 就是查全部错误
#还可以在此后加else 为当无错误产生时，正常代码的输出结果
#finally语句特别强大 无论错误与否其后语句都会被执行
class ShoppingList:
#这是在创建字典 像{‘牙刷‘：5，}
    def __init__(self,shopping_list):
        self.shopping_list = shopping_list
    def item_count (self):
        return len(self.shopping_list)
#返回购物清单上有几件商品
    def item_price(self):
        total_price = 0
        for price in self.shopping_list.values():
            total_price += price
            return total_price