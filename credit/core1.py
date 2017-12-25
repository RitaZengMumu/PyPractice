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

                                                                                                                                                     62,10        底端
                        return keywords

                    else:
                        return keywords
              else:
                  print('Wrong cardnumber or password,please input again')
                  Log_file.flush()
                  time.sleep(1)
                  Log_file.close
                  count +=1
              else:
              if count == 3

                  timesleep(1)
                  Log_file.close

return wrapper

#define the menu function,dispay the different menu according to the users

define menu(choice):
    if choice == '2'
        print ("please choose the service type:\n"
            "1.query the credit line \n"
            "2.credit card repayment \n"
            "3.credit card withdaw \n"
            "4.modify the password \n"
            "5.credit card transfer \n"
            "6.credit card statement \n"
            "7.easy shopping \n"
            "8.press the Q key to exit \n")
         service_items = input('-->')
    else:
        print("please choose the service type: \n"
            "a.modify the credit line \n"
            "b.add the new credit card user \n"
            "c.delete the credit card user \n"
            "d.modify the password \n"
            "e.press the Q key to exit \n")
         service_items = input('-->')
         exit()
    return service_items

#define the user data function

def get_user_data():
    with open(Base_dir + "\data\\user_db..txt",'r+',encoding='utf-8') as f:
        user_data=json.load(f)
    return user_data

#define the users data variable

user_data = get_user_data ()

#define the users's credit line function

@auth
def get_user_credit():
    user_credit = user_data[user_id]['Credit']
    print("Your current credit line is : %s RMB \n"
        %(user_credit))
    time.sleep(2)
    return user_credit


#define the repayment function

@auth
def repayment():
    user_data = get_user_data ()
    user_credit = int (user_data[user_id]['Credit'])
    user_balance = int (user_data[user_id]['Balance'])
    user_bill = user_Credit - user_balance
    print("The amount you need to pay back is : %s RMB" % user_bill)
    Exit_flag=True
    while Exit_flag:
        repayment_value = input ("please input the repayment amount:")
        if repayment_value.isdigit ():
            repayment_value = int (repayment_value)
            f = open(Base_dir + "\data\\user_db.txt",'r+',encoding='utf-8')
            json.dump(user_data,f)
            f.close()
            time.sleep(1)
            Exit_flag = False
            return repayment_value
        else:
            print ("please input the right amount")

#define the credit withdraw funtion

@auth
def enchament():
    user_credit = user_data[user_id]['Credit']
    print ("Your current availabe credit line is : %s" % user_credit)
    Exit_flag=True
    while Exit_flag:
        enchashment_value = input ("please input the amount you want to withdraw:")
        if enchashment_value.isdigit():
            enchashment_value = int (enchashment_value)
            if enchashment_value % 100 == 0:
                if enchashment_value <= user_credit :
                    user_data[user_id]['Balance'] = user_credit - enchashment_va
lue
                    f = open(Base_dir + "\data\\user_db.txt",'r+',encoding='utf-8')
                    json.dump(user_data, f)
                    f.close()
                    print("Withdrawed successfull,your current available credit line is : %s" % user_data[user_id]['Balance'])
                     time.sleep(1)
                     Exit_flag = False
                     return enchashment_value
                 else:
                     print("Your withdraw amount must can not bigger than your currant available line")
              else:
                  print("the withdraw amount must be int times of 100")
          else:
               print("Wrong input,the input must be int,and int times of 100")

#define the transfer
@auth
def transfer()
    user_balance = user_data[user_id]['Balance']
    print("Your current available credit line is : %s" % user_balance)
    Exit_flag=True
    while Exit_flag:
        transfer_user_id = input("please input the account you want transfer to:")
        transfer_value = input("please input the transfer amount:")
        if transfer_user_id in user_data.keys():
            while Exit_flag:
                if transfer_value.isdigit():
                    while Exit_flag:            

                        transfer_value=int(transfer_value)
                        user_passwd = input("please input the passwd to verify:")
                        if user_passwd == user_data[user_id]['Password']:
                        user_balance = user_balance - transfer_value
                        user_data[transfer_user_id]['Balance'] = int(user_data[transfer_user_id]['Balance']) + tansfer_value
                        f = open(Base_dir + "\data\\user_db.txt",'r+',encoding='uft-8')
                        json.dump(user_data, f)
                        f.close()
                        print("transfered successfull,your current available credit line is : %s" % user_balance)
                        time.sleep(1)
                        Exit_flag = False
                        return transfer_value
                    else:
                        print("password error,please input again")
                else:
                    print("Your must input int number")
            else:
                print("The account doesn't exist")

#define the credit inquery function

@auth

def billing_query():
    print("We just provide the bill query function")
    print("Your bill is : \n")
    Bill_log_file = opne(Base_dir + '\logs\\bill_log.txt','r',encoding='utf-8')
    for lines in Bill_log_file:
        if user_id in lines:
            print(lines.strip())
    print()
    time.sleep(1)

#define credit line modify function

def change_user_credit():
    print("You are modifying the credit line.")
    Exit_flag=True
    while Exit_flag:
        target_user_id=input("Please input the cardnumber:")
        if target_id in user_data.keys():
            while Exit_flag:
                new_credit = input("please input the new credit line" \n)
                if new_credit.isdigit():
                    new_credit = int(new_credit)
                    user_data[target_user_id]['Credit'] = new_credit
                    print("cardnumber %s credit line is %s " %(traget_user_id,new_credit))
                    choice = input ("please press 1 to make sure or press any other to cancel \n")
                    if choice == '1'
                        f= open(Base_dir + "\data\\user_db.txt", 'r+',encoding='utf-8')
                        json.dump(user_Data, f)
                        f.close()
                        print("Credit line is modified sucessfully,new credit line is effective")
                        time.sleep(1)
                        Exit_flag = False
                    else:
                         print("Credit line is not changed!")
               else:
                    print ("The cardnumber doesn't exist")

#define the password function

@auth

def change_pwd():
    print("Attention:modifying password")
    Exit_flag = True
    while Exit_flag:
        old_pwd = input("please input the current password!")
        if old_pwd == get_user_data[][]
