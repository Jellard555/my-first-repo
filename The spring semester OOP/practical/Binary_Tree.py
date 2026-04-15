class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


#前序遍历：根 左 右
def preorder(node):
    if node:
        print(node.val,end = "")
        preorder(node.left)
        preorder(node.right)
        
#中序遍历 左 根 右
def inorder(node):
    if node:
        inorder(node.left)
        print(node.val,end = "")
        inorder(node.right)

#后序遍历 左 右 根
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.val,end = "")

#层序遍历，广度优先
from collections import deque
def levelorder(node):
    if not node:
        return
    q = deque([node])
    while q:
        cur = q.popleft()
        print(cur.val,end = "")
        if cur.left:
            q.append(cur.left)
        if cur.right:
            q.append(cur.right)



#欧拉遍历
def euler_tour(node):
    if not node:
        return
    
    print(node.val)
    euler_tour(node.left)

    print(node.val)
    euler_tour(node.right)

    print(node.val)
#欧拉遍历 = 绕着树走一圈
#行走路线（按箭头走）：
# 1.从上面下来 → 第一次碰到 A
# 2.向左走到 B
# 3.从上面下来 → 第一次碰到 B
# 4.B 没有左孩子，回头向上 → 第二次碰到 B
# 5.B 没有右孩子，回头向上 → 第三次碰到 B
# 6.回到 A
# 7.向右走之前 → 第二次碰到 A
# 8.向右走到 C
# 9.从上面下来 → 第一次碰到 C
# 10.C 无孩子，回头向上 → 第二次碰到 C
# 11再回头向上 → 第三次碰到 C
# 12.回到 A → 第三次碰到 A

if __name__ == "__main__":
    #       A
    #      / \
    #     B   C
    root = Node("A")
    root.left = Node("B")
    root.right = Node("C")
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("=== 开始欧拉遍历 ===")
    euler_tour(root)

    print("前序：", end=""); preorder(root)    # 1 2 4 5 3
    print("\n中序:", end=""); inorder(root)   # 4 2 5 1 3
    print("\n后序:", end=""); postorder(root) # 4 5 2 3 1
    print("\n层序:", end=""); levelorder(root)