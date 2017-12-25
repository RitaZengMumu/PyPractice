"""def addlist(alist):
    for i in alist:
        yield i + 1
alist = [1, 2, 3, 4]
for x in addlist(alist):
    print x,


def h():
    print 'To be brave'
    yield 5
h()
"""
def h():
    print 'wen chuan',
    m = yield 5
    print m
    d = yield 12
    print 'we are together!'
c = h()
m = c.next()
d = c.send('Fighting!')
print 'we will never forget the date',m,'.',d