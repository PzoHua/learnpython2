# 练习字符串（string）和文本的用法
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious 
w = "This is the left side of..."
e = "a string with a right side."

print w+e


#输出结果
PS C:\work> python ex6.py
There are 10 types of people.
Those who know binary and those who don't.
I said: 'There are 10 types of people.'.
I also said: 'Those who know binary and those who don't.'.
Isn't that joke so funny?! False
This is the left side of...a string with a right side.
PS C:\work>

#一个问题
%r 表示打印全部
那么为什么输出的不是"There are %d types of people." % 10
而是'There are 10 types of people.'  
双引号打印成单引号， % 10 没有打印？？？
