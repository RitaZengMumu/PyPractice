# _*_ coding:utf-8 _*_
from gevent import monkey;

monkey.patch_all ()
import gevent
import urllib


def f(url):
    print('GET: %s' % url)
    resp = urllib.urlopen (url)
    data = resp.read ()
    print('%d bytes received from %s.' % (len (data), url))


gevent.joinall ([
    gevent.spawn (f, 'https://www.python.org/'),
    gevent.spawn (f, 'https://www.yahoo.com/'),
    gevent.spawn (f, 'http://dig.chouti.com/all/hot/recent/1'),
])