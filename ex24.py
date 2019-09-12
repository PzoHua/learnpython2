#-*-coding=utf-8-*-

#输出提示用户
print "Let's practice everything."
#输出单引号、反斜杠、换行及退四个
print 'You\'d need to know \'but secapes with \\ that do \n newlines and \t tabs.'

#定义一个变量、三引号内多行输出 
poem = """
\tThe lovely world                      
with logic so firmly planted 
cannot discern \n the needs of love 
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

#输出定义的变量、 上下框
print "----------------------------------"
print  poem
print "----------------------------------"


#定义变量five
five = 10 - 2 + 3 - 6
#通过格式化控制字符输出变量及提示
print "This should be five: %s" % five

#定义一个函数 secret_fromula ,通过一个变量传递至函数中
def secret_formula(started):
    jelly_beans = started * 500      #变量乘500
    jars = jelly_beans / 1000        #除10000
    crates = jars / 100              #除100
    return jelly_beans, jars, crates #返回结果
	
#定义一个变量
start_point = 10000
#将变量start_point通过函数名secret_formula传递到定义的函数中
#从函数secret_formula()中返回来的三个参数依次赋予左边的变量
beans, jars, crates  = secret_formula(start_point)   

#输出开始的点为：10000
print "With a starting point of: %d" % start_point
#输出返回的三个变量
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

#直接接收返回的值，不需要重新定义变量beans
print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
