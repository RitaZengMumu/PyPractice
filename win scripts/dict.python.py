#coding=utf-8
stu = {}
path = r"F:\video\contact.txt"
f = file(r"F:\video\stu.txt","r")
#f = file(r"/root/scripts/stu.txt","r")
for line in f.xreadlines():
    stu_id,stu_name,mail,company,title,phone=line.split()
    stu[stu_id] = [stu_name,mail,company,title,phone]
while True:
    query = raw_input('\033[32;1mplease input the query string\033[0m').strip()
    match_counter = 0
    for k,v in stu.items():
        if k.find(query) !=-1:
            index=k.find(query)
            print k[0:index] + '\033[32;1m %s\033[0m'% query+k[index+len(query):] ,v
            match_counter +=1

        else:
            str_v = '\t'.join (v)
            index=str_v.find(query)
            if index !=-1:
              print k,str_v[0:index] + '\033[32;1m %s\033[0m'% query+str_v[index+len(query):]
              match_counter +=1

    print 'matched \033[31;1m%s\033[0mrecords' % match_counter

