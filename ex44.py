# _*_coding=utf-8_*_

# 继承(Inheritance)VS合成(Composition)
# 大部分使用继承的场合都可以用合成取代，而多级继承需要不惜一切地避免之。

# 什么是继承：
# 继承的用处，就是用来指明一个类的大部分或全部功能，都是从一个父类中获取的。
# 当你写 class Foo(Bar)时，代码就发生了继承效果，这句话的意思时“创建一个叫
# Foo 的类，并让它继承 Bar 这个原先创建的类。Python语言会让 Bar 的实例所具
# 有的功能都工作在 Foo 的实例上。这样可以让你把通用的功能放到 Bar 里边，然
# 后再给 Foo特别设定一些功能。
# 当你这么做的时候，父类和子类有三种交互方式：
# 1.子类上的动作完全等同于父类上的动作
# 2.子类上的动作完全改写了父类上的动作
# 3.子类上的动作部分变更了父类上的动作

# 一、隐式继承(Implicit Inheritance)
# 当父类里定义了一个函数，但没有在子类中定义的例子，这是会发生隐式继承。

class Parent(object):
    
    def implicit(self):
        print "PARENT   implicit()"
        
class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

# class Child: 中的pass是在Python中创建空的代码区块的方法。这样就创建了一个叫
# Child的类，但在里面没有定义任何函数。在这里它将会从它的父类Parent中继承所有
# 的行为。运行结果：

# PARENT   implicit()
# PARENT   implicit()

# 就算在 Child里没有定义过implicit这个函数，这个函数依然可以工作，而且和父类 
# Parent中定义的行为一样。这就说明，如果那你将函数放到基类中(也就是这里的 Parent)，
# 那么所有的子类(也就是 Child这样的类)将会自动获得这些函数功能。如果你需要很多
# 类的时候，这样可以让你避免重复写很多代码。

# 二、显示覆写(Explicit Override)
# 有时候你需要让子类里的函数有一个不同的子类，这种情况下隐式继承是做不到，而你需要
# 覆写子类中的函数，从而实现它的新功能。你只要在子类 Child中定义一个相同名称的函数
# 就可以了，如下所示：

class Parent(object):
    
    def override(self):
        print "PARENT override()"

class Child(Parent):

    def override(self):
        print "CHILD override()"

dad = Parent()
son = Child()

dad.override()
son.override()

# 运行情况：

# PARENT override()
# CHILD override()

# 子类中定义的函数在这里取代了父类里的函数。

# 三、在运行前或运行后覆写

class Parent(object):
    
    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    def altered(self):
        print "CHILD, BEFROE PARENT altered()"
        super(Child, self).altered()            # 调用super并且加上 Child和 self这两个参数，在此基础上然后调用 altered。
        print "CHILD, AFTER PARENT altered()"
        
dad = Parent()
son = Child()

dad.altered()
son.altered()

# ----运行结果:---- #
# PARENT altered()
# CHILD, BEFROE PARENT altered()
# PARENT altered()
# CHILD, AFTER PARENT altered()
# ----------------- #

# 三、一起使用三种方式

# Make a class named Parent that is-a object.
class Parent(object):
    # class Parent has-a override function , and call it with self parameters.
    def override(self):
        print "PARENT override()"

    def implicit(self):
        print "PARENT implicit()"
        
    def altered(self):
        print "PARENT altered()"
    
class Child(Parent):
    
    def override(self):
        print "CHILD override()"
    # class Child has-a altered function that takes self parameters.
    def altered(self):
        print "CHILD, BEFORE PARNET altered()"
        super(Child, self).altered()    # 调用super并且加上 Child和 self这两个参数， 在此基础上然后调用 altered函数。
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

# 四、多重继承
# 多重继承是指你定义的类继承了多个类，如：
# class SuperFun(Child, Badstuff):
#    pass

# 这相当于说“创建一个叫 SuperFun 的类，让它同时继承 Child和 Badstuff”。
# 这里一旦你在 SuperFun 的实例上调用任何隐式动作， Python就必须回到类的层次结构中
# 去检查Child和 Badstuff，而且必须要用固定的次序去检查。为实现这一点 Python使用了
# 一个叫 “方法解析顺序(Method Resolution Order, MRO)”的东西，还用了一个叫C3的算法。

# 由于有这个太复杂的MRO和这个很好的算法， Python总不该把这些事情留给你去做，不然你
# 不就跟着头大了？所以Python给你这个 super()函数，用来在各种需要修改的场合为你处理，
# 有了super(),就再也不用担心把继承关系弄糟，因为Python会找到正确的函数。

# 五、super()和 __init__搭配使用
# 最常见的super()的用法是在基类的 __init__函数中使用。通常这也是唯一可以进行这种操
# 作的地方，在这里你在子类里做了一些事情，然后完成对父类的初始化。这里是一个在Child
# 中完成上述行为的例子：
class Child(Parent):

    def __init__(self, stuff):
        self.stuff = stuff
        super(Child, self).__init__()

# 这和上面的 Child.altered差别不大，只不过我在__init__里边先设置了个变量，然后才用
# Parent.__init__初始化了 Parent。

# 六、合成
# 继承是一种有用的技术，不过还有一种实现相同功能的方法，就是直接使用别的类和模块，
# 而非依赖于继承。如果你回头看的话，我们有三种继承的方式，但有两种会通过新代码取代
# 或者修改父类的功能。
# 这其实很容易地调用模块里的函数来实现
print "\n"
class Other(object):

    def override(self):
        print "OTHER override()"
        
    def implicit(self):
        print "OTHER implicit()"
    
    def altered(self):
        print "OTHER altered()"

class   Child(object):

    def __init__(self):
        self.other = Other()
    
    def implicit(self):
        self.other.implicit()
    
    def override(self):
        print "CHILD override()"
    
    def altered(self):
        print "CHILD, BEFROE OTHER altered()"
        self.other.altered()
        print "CHILD, AFTER OTHER altered()"
        
son = Child()

son.implicit()
son.override()
son.altered()

# 运行结果：
# -------------------
# OTHER implicit()
# CHILD override()
# CHILD, BEFROE OTHER altered()
# OTHER altered()
# CHILD, AFTER OTHER altered()
# -------------------

# 可以看出，child和Other里的大部分内容是一样的，唯一不同的是必须定义一个 Child.implicit
# 函数来完成它的功能。










