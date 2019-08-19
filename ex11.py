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
