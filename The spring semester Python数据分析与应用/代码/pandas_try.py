import pandas as pd
import numpy as np
'''d = pd.Series([5,6,2,30,4],index=["c","d","a","b","e"])
e = pd.Series([1,2,3,6],["a","f","h","d"])
d.name = "lllll"
d.index.name = 'ppp'
print(d.values)
print(d.index)
d["a"] = 20
print(d)'''
'''a = pd.DataFrame(np.arange(10).reshape(2,5))'''
dt = {"one":pd.Series([1,2,3],index = ["a","f","h"]),
        "two":pd.Series([9,7,6,22],index = ["a","f","h","d"])}
a = pd.DataFrame(dt)
c = pd.DataFrame(dt,index=["a","f","h"],columns=[111,"two","one"])
'''print(c)'''
dl = {'城市': ['北京', '上海','广州','深圳','沈阳'],
     '环比': [101.5, 101.2, 101.3, 102.0, 100.1],
     '同比': [120.7, 127.3, 119.4, 140.9, 101.4],
     '定基': [121.4,127.8, 120.0, 145.5, 101.6]}
d = pd.DataFrame(dl,index = ['c1', 'c2', 'c3', 'c4', 'c5'])
d = d.reindex(index=['c5', 'c4', 'c3', 'c2', 'c1'])
d = d.reindex(columns=['城市','定基','环比','同比'])
print(d)
