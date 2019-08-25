#coding=utf-8
#练习读写文件
from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")                #输入CRTL-C(^C)或者回车

print "Opening the file..."
target = open(filename, 'w')  #以写的模式打开目标文件，该模式会覆盖原文件内容--->>>命令：open（filename,'w')，需要一个open返回来接受的参数变量

print "Truncating the file.  Goodbye!"
target.truncate()   #以open返回来的参数变量传递文件，执行truncate（）命令

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")  #输入三个变量
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)            #将输入的三个变量的内容写入文件中
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()                #关闭文件（ps：若不关闭，则文件任占内存）

-------------------------------------------------------------------------
-------------------------------------------------------------------------
一个练习：第27行到32行文件重复太多，试着用一个target.write(),写入line1,line2,line3的内容。
定义一个变量，将line1、line2、line3的内容赋给新定义的变量
line123 = "%s\n %s\n %s\n" % (line1, line2, line3)
target.write(line123)
