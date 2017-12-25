# _*_ coding:utf-8 _*_

import importlib

b = importlib.import_module('lib.aa')

print(b.C().name)


"""f = __import__('lib.aa')
obj = f.aa.C()

print obj.name """