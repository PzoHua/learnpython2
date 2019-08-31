def add(a, b):                              #定义函数add， 需两个参数
    print "ADDING %d + %d" % (a, b)         #输出两个参数正在相加
    return a + b                            #将a+b的值返回给函数名

def subtract(a, b):                         #定义函数subtract， 需两个参数
    print "SUBSSTRACTING %d - %d" % (a, b)  #输出两个参数正在相减
    return a - b                            #将a -b 的值返回函数名

def multiply(a, b):                         #定义函数multiply，需要两个参数调去该函数
    print "MULTIPLYing %d * %d" % (a, b)    #输出两个参数正在相乘
    return a * b                            #将a*b 的值返回给函数名

def divide(a, b):                           #定义函数divide， 需两个参数   
    print "DIVIDEING %d / %d" % (a, b)      #输出两个参数正在相除
    return a / b                            #将a / b 的值返回给函数名


print "Let's do some math with just functions!"                     #输出这个程序的作用

age = add(30, 5)                        #通过函数名(add)调用函数(add),并给两个参数a=30, b=5;将结果返回给age变量
height = subtract(78, 4)                #通过函数名(subtract)调用函数(subtract),并给两个参数a=78, b=4;将结果返回给height变量
weight = multiply(90, 2)                #通过函数名(subtract)调用函数(subtract),并给两个参数a=90, b=2;将结果返回给weight变量
iq = divide(100, 2)                     #通过函数名(divdide)调用上面定义的函数(divide),并给两个参数a=100, b=2;将结果返回给iq变量

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)                 #输出返回值


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."                                               #提示用户

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))      #1.add函数调用subract函数；2.subract函数调用mltiply函数；
                                                                        #3.multiply函数调用divide函数；4.divide函数调用iq函数
print "That becomes: ", what, "Can you do it by hand?"                  #打印what结果；提示用户
