# _*_ coding:utf-8 _*_
import re
def mysplit(s,ds):
    res = [s]
    for d in ds:
        t=[]
        map(lambda x:t.extend(x.split(d)),res)
        res = t
    return res
s = 'ab;cdd,ggg|ggr\rrrg/ggr;fb,gg?ggrt3\ff'
print mysplit(s,';,|\t')

