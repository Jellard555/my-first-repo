from collections.abc import MutableMapping
import random

class MapBase(MutableMapping):
    class _Item:
        __slots__ = '_key' , '_value'
        def __init__(self,k,v):
            self._key = k
            self._value = v

class UnsortedTableMap(MapBase):
    def __init__(self):
        self._table = []
    def __getitem__(self, k):
        for item in self._table:
            if item._key == k:
                return item._value
        raise KeyError(k)
    def __setitem__(self,k,v):
        for item in self._table:
            if item._key == k:
                item._value == v
            return
        self._table.append(self._Item(k,v))
    def __delitem__(self, k):
        for i in range(len(self._table)):
            if self._table[i]._key == k:
                self._table.pop(i)
                return
        raise KeyError(k)
    def __len__(self):
        return len(self._table)
    def __iter__(self):
        for item in self._table:
            yield item._key

class HashMapBase(MapBase):
    def __init__(self,cap=11,p=109345121):
        self._table = [None] * cap
        self._n = 0
        self._prime = p
        self._scale = 1 + random.randrange(p-1)
        self._shift = random.randrange(p)

    def _hash_function(self,k):
        hash_code = hash(k)
        return (hash_code * self._scale + self._shift) % self._prime % len(self._table)
    def __len__(self):
        return self._n
    def _load_factor(self):
        return self._n / len(self._table)
    def _resize(self,new_cap):
        old_items = list(self.items())
        self._table = [None] * new_cap
        self._n = 0
        for k,v in old_items:
            self[k] = v

    def __getitem__(self,k): raise NotImplementedError
    def __setitem__(self,k,v): raise NotImplementedError
    def __delitem__(sefl,k): raise NotImplementedError

class ChainHashMap(HashMapBase):
    def _bucket_getitem(self,j,k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError(k)
        return bucket[k]
    
    def _bucket_setitem(self,j,k,v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()
        key_exists = True
        try:
            self._table[j][k]
        except KeyError:
            key_exists = False
        self._table[j][k] = v
        if not key_exists:
            self._n += 1
            if self._load_factor() > 0.5:
                self._resize(2 * len(self._table) - 1)
    def _bucket_delitem(self,j,k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError(k)
        del bucket[k]
        self._n -= 1

    def __getitem__(self,k):
        j = self._hash_function(k)
        return self._bucket_getitem(j,k)
    
    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j,k,v)
    def __delitem__(self,k):
        j = self._hash_function(k)
        self._bucket_delitem(j,k)
    
    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key

if __name__ == '__main__':
    m = ChainHashMap()

    # 插入
    m['a'] = 1
    m['b'] = 2
    m['c'] = 3
    m['d'] = 4
    m['e'] = 5
    m['f'] = 6
    m['g'] = 7

    print("元素个数:", len(m))
    print("负载因子:", round(m._load_factor(), 2))
    print("当前容量:", len(m._table))
    print("m['a'] =", m['a'])
    print(list(m.keys()))