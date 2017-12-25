#!/bin/python
#coding=utf-8
goods=['iphone','car','bike','watch','coffee']
prices=[4800,500000,200,10000,48]
shopping=[]
money=int(raw_input('please input your salary:'))
while min(prices)<=money:
  for i in range(len(goods)):
    print goods[i],prices[i]
  buy=raw_input('please choose what you want to buy:').strip()
  if len(buy) == 0:
    print "you must input the name of goods"
    continue
  elif buy not in goods:
    print 'You must input a valid goods'
    continue
  else:
    print 'You have choosed %s' % buy
    j=goods.index(buy)
    price=prices[j]
  if price>money:
      print 'Your money is less than the price %s' % price
  else:
    money=money-price
    shopping.append (buy)
    del goods[j]
    del prices[j]
    print 'your left money is %s' % money
    print 'you have bought %s' % shopping

