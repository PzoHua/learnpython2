#_*_coding=utf-8_*_

from sys import exit
import room1

# 登陆账号密码
def login():

    print "登陆深渊账号:"
    account = raw_input("> ")
    print "输入黑暗密码"
    password = raw_input("> ")
    
    if account in dict.keys() and password == dict['%s' % account]:
            print "欢迎%s来到黑暗魔兽深渊" % account
            room = room1.dog_room()
            room.beef()
            
    elif account in dict.keys() and password != dict['%s' % account]:
        print "密码不正确,请重新输入\n"
        login()

    else:
        failed()

# 注册新账号      
def new_user():

    new_account = raw_input("输入新账号：")
    new_password = raw_input("输入新密码: ")
    dict['%s' % new_account] = "%s" % new_password
    print "注册成功！"
    login()

# 登陆失败
def failed():
    
    print "用户不存在!"
    print "按1重新登陆！"
    print "按2注册新账号！"
    
    while True:
        next = raw_input("> ")
        if next == '1' :
            login()
        elif next == '2':
            new_user()
        else:
            print "请输入数字1 or 2"


# 账号密码字典；
dict = {
    #'name': 'password',
    'admin': 'admin'
    }

print "欢迎来到黑暗尽头!"

next = raw_input("按enter开始游戏......")
if next == "":
    print "#1 登陆账号密码"
    print "#2 注册新账号\n"

    while True:
        next = raw_input("> ")
        if next == '1':
            login()
        elif next == '2':
            new_user()
        else:
            print "请输入正确的数字"

else:
    exit(0) 
