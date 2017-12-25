#_*_ coding:utf-8 _*_
import os,sys,time
Base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(Base_dir)
str="欢迎使用银行信用卡自助服务系统！\n"
for i in str:
  sys.stdout.write(i)
  sys.stdout.flush()
  time.sleep(0.1)
while True:
  print("1、管理人员入口。")
  time.sleep(0.3)
  print("2、用户登录入口。")
  print("3、退出请按q!")
  choice=input(":")
  from core import main
  Exit_flag=True
  while Exit_flag:
    user_choice=main.menu(choice)
    if user_choice == '1':
      main.get_user_credit()
    elif user_choice == '2':
      main.repayment()
    elif user_choice == '3':
      main.enchashment()
    elif user_choice == '4':
      main.change_pwd()
    elif user_choice == '5':
      main.transfer()
    elif user_choice == '6':
      main.billing_query()
    elif user_choice == '7':
      print("该功能正在建设中，更多精彩，敬请期待！")
    elif user_choice == 'a':
      main.change_user_credit()
    elif user_choice == 'b':
      main.add_user()
    elif user_choice == 'c':
      main.del_user()
    elif user_choice == 'd':
      main.change_pwd()
    elif user_choice == 'q' or user_choice == 'Q':
      print("欢迎再次使用，再见！")
      Exit_flag = False

# Author by Andy
# _*_ coding:utf-8 _*
import json, sys, os, time, shutil

Base_dir = os.path.dirname (os.path.dirname (os.path.abspath (__file__)))
sys.path.append (Base_dir)


# 定义认证装饰器
def auth(func):
    def wrapper(*args, **kwargs):
        # print("请输入卡号和密码进行验证！")
        f = open (Base_dir + '\data\\user_db.txt', 'r')
        Log_file = open (Base_dir + '\logs\log.txt', 'a+', encoding='utf-8')
        Bill_log_file = open (Base_dir + '\logs\\bill_log.txt', 'a+', encoding='utf-8')
        func_name = func.__name__
        Time_formate = '%Y-%m-%d  %X'
        start_time = time.strftime (Time_formate, time.localtime ())
        user_data = json.load (f)
        count = 0
        while count < 3:
            global user_id
            global user_pwd
            user_id = input ('请输入您的卡号:')
            user_pwd = input ('请输入您的密码:')
            if user_id in user_data:
                if user_pwd == user_data[user_id]['Password']:
                    Log_file.write (start_time + ' 卡号 %s 认证成功!\n' % user_id)
                    Log_file.flush ()
                    time.sleep (1)
                    Log_file.close
                    keywords = func (*args, **kwargs)
                    if func_name == 'repayment' or func_name == 'transfer' or func_name == 'enchashment':
                        Bill_log_file.write (
                            start_time + ' 卡号 ' + user_id + ' 发起 ' + func_name + ' 业务，金额为： %s \n' % keywords)
                        Bill_log_file.flush ()
                        time.sleep (1)
                        Bill_log_file.close
                        return keywords
                    else:
                        return keywords
                else:
                    print('卡号或密码错误！请重新输入！')
                    Log_file.write (start_time + ' 卡号 %s 认证失败!\n' % user_id)
                    Log_file.flush ()
                    time.sleep (1)
                    Log_file.close
                    count += 1
            else:
                print("卡号不存在，请确认！")
            if count == 3:
                print("对不起,您已输错3三次，卡号已锁定！")
                Log_file.write (start_time + ' 卡号 %s 因连续三次验证失败而被锁定！\n' % user_id)
                time.sleep (1)
                Log_file.close

    return wrapper


# 定义菜单函数，根据不同用户显示不通菜单。

def menu(choice):
    if choice == '2':
        print("请选择服务类别:\n"
              "1、查询信用额度。\n"
              "2、信用卡还款。\n"
              "3、信用卡提现。\n"
              "4、修改口令。\n"
              "5、信用卡转账。\n"
              "6、信用卡账单查询。\n"
              "7、轻松购物。\n"
              "8、退出请按q!\n")
        service_items = input ('-->')
    elif choice == '1':
        print("请选择服务类别:\n"
              "a、修改用户信用额度。\n"
              "b、新增信用卡用户。\n"
              "c、删除信用卡用户。\n"
              "d、修改用户口令。\n"
              "e、退出请按q!\n")
        service_items = input ('-->')
    else:
        print("感谢使用，祝生活愉快！")
        exit ()
    return service_items


# 定义备份用户数据文件函数
def back_up_file():
    Time_formate = '%Y-%m-%d'
    Sys_time = time.strftime (Time_formate, time.localtime ())
    shutil.copy (Base_dir + "\data\\user_db.txt", Base_dir + "\data\\user_db--" + Sys_time + ".bak.txt")


# 定义获取用户数据信息函数
def get_user_data():
    with open (Base_dir + "\data\\user_db.txt", 'r+', encoding='utf-8') as f:
        user_data = json.load (f)
    return user_data


# 定义用户数据变量
user_data = get_user_data ()


# 定义查询信用额度函数
@auth
def get_user_credit():
    user_credit = user_data[user_id]['Credit']
    print("您目前的信用额度为：%s元\n"
          % (user_credit))
    time.sleep (2)
    return user_credit


# 定义信用卡还款函数
@auth
def repayment():
    user_data = get_user_data ()
    user_credit = int (user_data[user_id]['Credit'])
    user_balance = int (user_data[user_id]['Balance'])
    user_bill = user_credit - user_balance
    print("您目前需要还款金额为：%s元.\n" % user_bill)
    Exit_flag = True
    while Exit_flag:
        repayment_value = input ("请输入还款金额：")
        if repayment_value.isdigit ():
            repayment_value = int (repayment_value)
            user_data[user_id]['Balance'] = user_data[user_id]['Balance'] + repayment_value
            f = open (Base_dir + "\data\\user_db.txt", 'r+', encoding='utf-8')
            json.dump (user_data, f)
            f.close ()
            print("恭喜，还款成功！")
            print("您目前需要还款金额为：%s元.\n" % (user_data[user_id]['Credit'] - user_data[user_id]['Balance']))
            time.sleep (1)
            Exit_flag = False
            return repayment_value
        else:
            print("请输入正确的金额！")


# 定义信用卡提现函数
@auth
def enchashment():
    user_credit = user_data[user_id]['Credit']
    print("你可用的取现额度为：%s" % user_credit)
    Exit_flag = True
    while Exit_flag:
        enchashment_value = input ("请输入您要取现的金额：")
        if enchashment_value.isdigit ():
            enchashment_value = int (enchashment_value)
            if enchashment_value % 100 == 0:
                if enchashment_value <= user_credit:
                    user_data[user_id]['Balance'] = user_credit - enchashment_value
                    f = open (Base_dir + "\data\\user_db.txt", 'r+', encoding='utf-8')
                    json.dump (user_data, f)
                    f.close ()
                    print("取现成功，您目前的可用额度为：%s" % user_data[user_id]['Balance'])
                    time.sleep (1)
                    Exit_flag = False
                    return enchashment_value
                else:
                    print("您的取现额度必须小于或等于您的信用额度！")
            else:
                print("取现金额必须为100的整数倍！")
        else:
            print("输入有误，取现金额必须为数字，且为100的整数倍")


@auth
# 定义信用卡转账函数
def transfer():
    user_balance = user_data[user_id]['Balance']
    print("您目前的可用额度为：%s" % user_balance)
    Exit_flag = True
    while Exit_flag:
        transfer_user_id = input ("请输入对方帐号：")
        transfer_value = input ("请输入转账金额：")
        if transfer_user_id in user_data.keys ():
            while Exit_flag:
                if transfer_value.isdigit ():
                    while Exit_flag:
                        transfer_value = int (transfer_value)
                        user_passwd = input ("请输入口令以验证身份：")
                        if user_passwd == user_data[user_id]['Password']:
                            user_balance = user_balance - transfer_value
                            user_data[transfer_user_id]['Balance'] = int (
                                user_data[transfer_user_id]['Balance']) + transfer_value
                            f = open (Base_dir + "\data\\user_db.txt", 'r+', encoding='utf-8')
                            json.dump (user_data, f)
                            f.close ()
                            print("转账成功，您目前的可用额度为：%s" % user_balance)
                            time.sleep (1)
                            Exit_flag = False
                            return transfer_value
                        else:
                            print("密码错误，请重新输入！")
                else:
                    print("转账金额，必须为数字，请确认！")
        else:
            print("帐号不存在，请确认！")


# @auth
# 定义信用卡账单查询函数
@auth
def billing_query():
    print("我们目前仅提供查询所有账单功能！")
    print("您的账单为：\n")
    Bill_log_file = open (Base_dir + '\logs\\bill_log.txt', 'r', encoding='utf-8')
    for lines in Bill_log_file:
        if user_id in lines:
            print(lines.strip ())
    print()
    time.sleep (1)


# 定义修改信用卡额度函数
def change_user_credit():
    print("您正在修改用户的信用额度！")
    Exit_flag = True
    while Exit_flag:
        target_user_id = input ("请输入您要修改的用户卡号：\n")
        if target_user_id in user_data.keys ():
            while Exit_flag:
                new_credit = input ("请输入新的信用额度：\n")
                if new_credit.isdigit ():
                    new_credit = int (new_credit)
                    user_data[target_user_id]['Credit'] = new_credit
                    print("卡号 %s 的新信用额度为：%s " % (target_user_id, new_credit))
                    choice = input ("确认请输入1或者按任意键取消：\n")
                    if choice == '1':
                        f = open (Base_dir + "\data\\user_db.txt", 'r+', encoding='utf-8')
                        json.dump (user_data, f)
                        f.close ()
                        print("信用额度修改成功，新额度已生效！")
                        print("卡号 %s 的新信用额度为：%s " % (target_user_id, user_data[target_user_id]['Credit']))
                        time.sleep (1)
                        Exit_flag = False
                    else:
                        print("用户的信用额度未发生改变！")
                else:
                    print("信用额度必须为数字！请确认！")
        else:
            print("卡号不存在，请确认！")


# 定义修改口令函数
@auth
def change_pwd():
    print("注意：正在修改用户密码！")
    Exit_flag = True
    while Exit_flag:
        old_pwd = input ("请输入当前密码：")
        if old_pwd == get_user_data ()[user_id]["Password"]:
            new_pwd = input ("请输入新密码：")
            new_ack = input ("请再次输入新密码：")
            if new_pwd == new_ack:
                user_data = get_user_data ()
                user_data[user_id]["Password"] = new_pwd
                f = open (Base_dir + "\data\\user_db.txt", 'r+', encoding='utf-8')
                json.dump (user_data, f)
                f.close ()
                print("恭喜，密码修改成功！")
                time.sleep (1)
                Exit_flag = False
            else:
                print("两次密码不一致，请确认！")
        else:
            print("您输入的密码不正确，请在确认！")


# 定义新增信用卡函数
def add_user():
    Exit_flag = True
    while Exit_flag:
        user_id = input ("user_id:")
        Balance = input ("Balance:")
        Credit = input ("Credit:")
        if Balance.isdigit () and Credit.isdigit ():
            Balance = int (Balance)
            Credit = int (Credit)
        else:
            print("余额和信用额度必须是数字！")
            continue
        Name = input ("Name:")
        Password = input ("Password:")
        print("新增信用卡用户信息为：\n"
              "User_id:%s\n"
              "Balance:%s\n"
              "Credit:%s\n"
              "Name:%s\n"
              "Password:%s\n"
              % (user_id, Balance, Credit, Name, Password))
        choice = input ("提交请按1，取消请按2,退出请按q：")
        if choice == '1':
            back_up_file ()
            user_data = get_user_data ()
            user_data[user_id] = {"Balance": Balance, "Credit": Credit, "Name": Name, "Password": Password}
            f = open (Base_dir + "\data\\user_db.txt", 'w+', encoding='utf-8')
            json.dump (user_data, f)
            f.close ()
            print("新增用户成功！")
            time.sleep (1)
            Exit_flag = False
        elif choice == '2':
            continue
        elif choice == 'q' or choice == 'Q':
            time.sleep (1)
            Exit_flag = False
        else:
            print('Invaliable Options!')


# 定义删除信用卡函数
def del_user():
    Exit_flag = True
    while Exit_flag:
        user_id = input ("请输入要删除的信用卡的卡号：")
        if user_id == 'q' or user_id == 'Q':
            print('欢迎再次使用，再见！')
            time.sleep (1)
            Exit_flag = False
        else:
            user_data = get_user_data ()
            print("新增信用卡用户信息为：\n"
                  "User_id:%s\n"
                  "Balance:%s\n"
                  "Credit:%s\n"
                  "Name:%s\n"
                  % (user_id, user_data[user_id]['Balance'], user_data[user_id]['Credit'], user_data[user_id]['Name']))
            choice = input ("提交请按1，取消请按2,退出请按q：")
            if choice == '1':
                back_up_file ()
                user_data.pop (user_id)
                f = open (Base_dir + "\data\\user_db.txt", 'w+', encoding='utf-8')
                json.dump (user_data, f)
                f.close ()
                print("删除用户成功！")
                time.sleep (1)
                Exit_flag = False
            elif choice == '2':
                continue
            elif choice == 'q' or choice == 'Q':
                print('欢迎再次使用，再见！')
                time.sleep (1)
                Exit_flag = False
            else:
                print('Invaliable Options!')