print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)


---------------------------------------------------------------------------------------------------
输出结果:
PS C:\work> python ex11.py
How old are you? 35
How tall are you? 6'22"
How much do you weight? 180lbs
So, you're '35' old, '6\'22"' tall and '180lbs' heavy.
PS C:\work>

---------------------------------------------------------------------------------------------------

这个程序的作用：
1.接受用户的输入；
2.改变输入；
3.打印出改变了的输入。

Note:
在每行print后面加了逗号（comma），以便不用每次print这一哈后都跑到下一行去。

注意到最后后一行'6\'2"'里多了\'序列。单引号需要被转义，从而防止它被识别为字符串的结尾。

补充：
  raw_input() 将所有输入作为字符串看待，返回字符串类型。
注意：input() 和 raw_input() 这两个函数均能接收字符串 ，
但 raw_input() 直接读取控制台的输入（任何类型的输入它都可以接收）。
而对于 input() ，它希望能够读取一个合法的 python 表达式，即你输入字符串的时候必须使用引号将它括起来，否则它会引发一个 SyntaxError 。
除非对 input() 有特别需要，否则一般情况下我们都是推荐使用 raw_input() 来与用户交互。
注意：python3 里 input() 默认接收到的是 str 类型。
