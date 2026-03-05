#assert 后面放布尔值 放我们认为布尔值为true的
#测试代码
#unittest
import unittest
from try12 import ShoppingList
class TestShoppingList(unittest.TestCase):
    def test_item_count(self):
        shopping_list = ShoppingList({'zhijin':8,'maojin':30,'tuoxie':15})
        self.assertEqual(shopping_list.item_count(),3)

