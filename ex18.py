# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1
	
# this one takes no arguments
def print_none():
    print "I got nothin'."


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
----------------------------------------------------------------------

1.首先，告诉python创建一个函数（defined）的缩写def
2.接着def的函数的名称 “print_two” （随便定义）
3.定义了的函数的参数，参数放在括号中
4.用：结束本行，下一行开头缩进4个空格表示属于这个函数的内容
5.：后的下面第一行作用是将参数解包，类似脚本参数解包
6.再下一行解包后打印每个参数

PS:函数print_two的问题是：它并不是创建函数最简单的方法。在Python函数中可以
跳过整个参数解包的过程，直接使用（）里边的名称作为变量名。接受参数可以是多个、
两个、一个或没有。
