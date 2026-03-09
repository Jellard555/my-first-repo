#assert 后面放布尔值 放我们认为布尔值为true的
#测试代码
#unittest
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
#返回总价