#coding=utf-8
money=int(raw_input('please input your salary:'))
products=[
        ['iphone',4800],
        ['car',500000],
        ['bike',200],
        ['watch',10000],
        ['coffee',48]
]

while True:
    for p in products:
        print products.index(p),p[0],p[1]
    choice=raw_input('\033[32;1m please choose sth to buy:\033[0m')
    print p[0]
