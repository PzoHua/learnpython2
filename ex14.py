# coding=utf-8 #防止出现非法字符串
#把sys模组import进来 
from sys import argv
#脚本（script），就是写的.py程序。 
#argv（"argumentn variable"）参数变量 要求用户在执行命令时就要输入参数
#需要输入两个变量参数才可以执行这个程序，第一个是脚本.py； 第二个是用户名（随便）
script, user_name = argv
#将用户提示符设置为变量prompt，这样我们就不需要在每次用到raw_input时重复输入提示用户的字符了。而且如果你要将提示符
#修改成别的字符，你只要改一个位置就可以了。
prompt = '> '
#通过格式控制字符输出两个参数变量
print "Hi %s, I'm the %s script." %(user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
#因为是在命令执行过程中要求用户输入，所以采用raw_input()而不是argv
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
#因为是在命令执行过程中要求用户输入，所以采用raw_input()而不是argv
lives = raw_input(prompt)

print "What kind of computer do you have?"
#因为是在命令执行过程中要求用户输入，所以采用raw_input()而不是argv
computer = raw_input(prompt)
#输出用户输入结果， （"""）可以多行输出，且前后空一行。
print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
