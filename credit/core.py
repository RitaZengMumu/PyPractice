#!/bin/python
#_*_coding:utf-8_*_
import json,sys,os,time,shutil
Base_dir=os.path.dirname(os.path.dirname(os.path.abspath(_file_)))
sys.path.append(Base_dir)
#定义认证装饰器
def auth(func):
    def wrapper(*args,**kwargs):
        #print("please input your card account and password!")
        f = open(Base_dir+'\data\\user_db.txt','r')
        Log_file = open(Base_dir+'\logs\log.txt','a+',encoding='utf-8')
        Bill_log_file = open(Base_dir + '\logs\\bill_log.txt', 'a+', encoding='utf-8')
        func_name = func._name_
        Time_formate = '%Y-%m-%d %X'
        start_time = time.strftime(Time_formate, time.localtime())
        user_data = json.load(f)
        count=0
        while count < 3:
            global user_id
            global user_pwd
            user_id = input('please input your card number:')
            user_pwd = input('please input your password:')
            if user_id in user_data:
                if user_pwd == user_data[user_id]['Password']:
                    Log_file.write(start_time + 'cardnumber %s verified sucessfull! \n' % user_id) 
                    Log_file.flush()
                    time.sleep(1)
                    Log_file.close
                    keywords = func(*args, **kwargs)
                    if func_name == 'repayment' or func_name == 'tranfer' or func_name == 'enchashment':
                        Bill_log_file.write(start_time + 'cardnumber' + used_id +' use' + func_name + 'business,the amount is: %s \n' % keywords)
                        Bill_log_file.flush()
                        time.sleep(1)
                        Bill_log_file.close
                        return keywords

                    else:
                        return keywords
              else:
                  print('Wrong cardnumber or password,please input again')
                  Log_file.wirte(start_time +'cardnumber %s verified failed \n' % user_id)
                  Log_file.flush()
                  time.sleep(1)
                  Log_file.close
                  count +=1
              else:
                  print ("your card number dosen't exist,please make sure you input the right cardnumber!")
              if count == 3
                  print ("sorry,you have input 3 times,your account has been locked")
                  Logfile.wirte(start_time + 'cardnumber %s is locked caused by 3 times failed verify' % user_id)

                  timesleep(1)
                  Log_file.close

return wrapper

#define the menu function,dispay the different menu according to the users

define menu(choice):
  if choice == '2'
    print ("please choose the service type:\n")
        ""
             
