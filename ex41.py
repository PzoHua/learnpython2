#_*_coding=utf-8_*_

# 定义类 类名TheThing
class TheThing(object):
	
	def __init__(self):       # 类初始化 创建
		self.number = 0
		
	def some_function(self):   # 类下属性之一 名为some_function 需要一个参数
		print "I got called."
	
	def add_me_up(self, more): # 类下属性之一 名为add_me_up 需要两参数
		self.number += more
		return self.number
		
# two different things
a = TheThing()     # 调用类  并在类中创建初始化a
b = TheThing()     # 调用类

a.some_function()  # 调用创建的a下的函数some_function()
b.some_function()

print a.add_me_up(20)  # 调用类下的属性add_me_up--->>>a.number = 20 将值返回
print b.add_me_up(30)

print a.number    # 调用类中的变量
print b.number

# Study this. This is how you pass a variable
# from one class to another. You will need this.
class TheMultiplier(object):

	def __init__(self, base):
		self.base = base
		
	def do_it(self, m):
		return m * self.base


x = TheMultiplier(a.number)  # 以另一个类中的变量作为这个类的参数：用TheMultiplier连接参数'x'和'20'(a.number) ---->>> 最终值 x=20

print x.do_it(b.number)      # 用类TheMultiplier中的函数do_it()连接两个参数 'x'('20')和 b.number('30') 运行第37行代码
