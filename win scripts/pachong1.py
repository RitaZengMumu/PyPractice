# _*_ coding:utf-8 _*_

import urllib
import requests
import gevent,time
from gevent import monkey

monkey.patch_all()

def f(url):
    print('GET: %s' % url)
    resp = urllib.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s' %(len(data),url))

urls = ['https://www.python.org/',
        'https://www.zhihu.com/',
        'http://dig.chouti.com/all/hot/recent/1'
]

time_start = time.time()
for url in urls:
    f(url)
print u"同步cost:", time.time() - time_start

async_time_start = time.time()
gevent.joinall([
    gevent.spawn(f, 'https://www.python.org/'),
    gevent.spawn(f, 'https://www.zhihu.com/'),
    gevent.spawn(f, 'http://dig.chouti.com/all/hot/recent/1')

])

print u"异步cost",time.time() - async_time_start