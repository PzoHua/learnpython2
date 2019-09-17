#_*_coding=utf-8_*_
# if 语句

people = 20 
cats = 30
dogs = 15


if people < cats:
    print "Too many cats! The world is doomed!"
	
if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"


dogs += 5 

if people >= dogs:
    print "People area greater than or equal to dogs."

if people <= dogs:
	print "People are less than or equal to dogs."

if people == dogs:
    print "People are equal dogs."

-----------------------------------------------------------------------
-----------------------------------------------------------------------
1.If对于它下一行的代码做什么？
If语句告诉你的脚本：“如果这个布尔表达式为真，就运行接下来的代码，否则跳过这一段。”

2.为什么if语句的下一行需要4个空格的缩进？
行尾的冒号的作用告诉Python接下来你要创建一个新的代码区段。这与创建函数模块一样。

3.如果不缩进，会发生什么事情？
如果你没有缩进，你应该会看到Python报错。Python的规则里，只要一行以“冒号（colon）”：
结尾，它接下来的内容应该有缩进。

4.把习题27中的其他布尔表达式放到if语句中会不会也可以运行呢？
试一下。可以。而且不管多复杂都可以，虽然写复杂的东西通常是一种不好的编程风格。

5.如果把变量people，carts，和dogs的初始值改掉，会发生什么事情？
因为你比较的对象是数字，如果把这些数字改掉的话，某些位置的if语句会被演绎为True，而它
下面的代码区段将被运行。

出处：《笨办法学Python》（第三版） 
(英文版地址：https://learnpythonthehardway.org/book/)  Zed Shaw--著

