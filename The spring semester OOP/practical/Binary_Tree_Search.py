from collections.abc import MutableMapping


class MapBase(MutableMapping):
    class _Item:
        __slot__ = '_key','_value'
        def __init__(self,k,v):
            self._key = k
            self._value = v

class LinkedBinaryTree:
    class Node:
        __slot__ = '_element' , '_parent' , '_left' , '_right' 
        def __init__(self,element,parent = None ,left = None, right = None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

        class Position:
            def __init__(self,container,node):
                self._container = container
                self._node  = node

            def key(self):
                return self._node._element._key
            def value(self):
                return self._node._element._value
            def __eq__(self, other):
                return type(other) is type(self) and other._node is self._node
            
        def __init__(self):
            self._root = None
            self._size = 0

        def _validate(self,p):
            if not isinstance(p,self.Position):
                raise TypeError('must be a position')
            if p._node._parent is p._node:
                raise ValueError("position is no longer valid")
            return p._node
        def _make_position(self,node):
            return self.Position(self,node) if node is not None else None
        def root(self):
            return self._make_position(self._root)
        def left(self,p):
            node = self._validate(p)
            return self._make_position(node._left)
        def right(self,p):
            node = self._validate(p)
            return self._make_position(node._right)
        def parent(self,p):
            node = self._validate(p)
            return self._make_position(node._parent)
        def num_children(self,p):
            node = self._validate(p)
            count = 0
            if node._left is not None:
                count += 1
            if node._right is not None:
                count += 1
            return count
        def _add_root(self,e):
            if self._root is not None:
                raise ValueError("root exists")
            self._root = self.Node(e)
            self._size = 1
            return self._make_position(self._root)
        def _add_right(self,p,e):
            node = self._validate(p)
            if node._right is not None:
                raise ValueError("right child exists")
            node._right = self.Node(e,node)
            self._size += 1
            return self._make_position(node._right)
        def _add_left(self,p,e):
            node = self._validate(p)
            if node._left is not None:
                raise ValueError("left child exists")
            node._left = self.Node(e,node)
            self._size += 1
            return self._make_position(node._left)
        def _replace(self,p,e):
            node = self._validate(p)
            old = node._element
            node._element = e
            return old
        
        def _delete(self,p):
            node = self._validare(p)
            if self.num_children(p) == 2:
                raise ValueError("two children can not delete")
            child = node._left if node._left else node._right
            if child is not None:
                child._parent = node._parent
            if node is self._root:
                self._root = child
            else:
                parent = node._parent
                if node is parent._left:
                    parent._left = child
                else:
                    parent._right = child
            self._size -= 1
            node._parent = node
            return node._element

class TreeMap(LinkedBinaryTree,MapBase):

    def __init__(self):
        LinkedBinaryTree.__init__(self)
        MapBase.__init__(self)

    def _subtree_search(self,p,k):
        if p.key() == k:
            return p
        elif k < p.key():
            if self.left(p) is not None:
                return self._subtree_search(self.left(p),k)
        else:
            if self.right(p) is not None:
                return self._subtree_search(self.right(p),k)
            return p
        
    def _subtree_first_position(self,p):
        walk = p
        while self.left(walk) is not None:
            walk = self.left(walk)
        return walk
    def _subtree_last_position(self,p):
        walk = p
        while self.right(walk) is not None:
            walk = self.right(walk)
        return walk
    
    def __getitem__(self,k):
        if self._root is None:
            raise KeyError(k)
        root_pos = self._make_position(self._root)
        p = self._subtree_search(root_pos,k)
        if p.key() != k:
            raise KeyError(k)
        return p.value()
    
    def __setitem__(self,k,v):
        item = self._Item(k,v)
        if self._root is None:
            self._add_root(item)
            return
        root_pos = self._make_position(self._root)
        p = self._subtree_search(root_pos,k)
        if p.key() == k:
            p._node._element._value = v
            return
        elif k < p.key():
            self._add_left(p,item)
        else:
            self._add_right(p,item)

    def __delitem__(self,k):
        if self._root is None:
            raise KeyError(k)
        root_pos = self._make_position(self._root)
        p = self._subtree_search(root_pos,k)
        if p.key() != k:
            raise KeyError(k)
        self._delete(p)
    def __len__(self):
        return self._size
    

    def __iter__(self):
        p = self.first()
        while p is not None:
            yield p.key()
            p = self.after(p)
    
    def first(self):
        return self._subtree_first_position(self.root()) if self._root else None
    def after(self,p):
        if self.right(p):
            return self._subtree_first_position(self.right(p))
        else:
            walk = p
            parent = self.parent(walk)
            while parent is not None and walk == self.right(parent):
                walk = parent
                parent = self.parent(parent)
            return parent
        

if __name__ == '__main__':
    bst = TreeMap()

    # 插入
    bst[5] = "A"
    bst[3] = "B"
    bst[7] = "C"
    bst[2] = "D"
    bst[4] = "E"
    bst[6] = "F"
    bst[8] = "G"

    print("中序遍历（有序）：", list(bst))
    print("查找 key=4:", bst[4])
    print("树大小：", len(bst))

    # 删除
    del bst[5]
    print("删除 5 后中序遍历：", list(bst))
