#coding=utf-8
name=raw_input("what's your name?").strip()
if len(name) == 0:
	print "You must input sth as name"

age =raw_input("how old are you?")
job =raw_input("what is your job? ")

msg="""
Information of %s as below:
	Name ：\033[42;1m%s \033[0m;
	Age  : %s
	Job  : %s
""" %(name,name,age,job)

if int(age) >=50:
	print "You are too old,you can only work for ..."
elif int(age) >=30:
	print "You are now in the middle age,so enjoy your life"

else:
	print "You are still very young"
	

print msg
