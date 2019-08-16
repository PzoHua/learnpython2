
formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
    "So I said goodnight."
)	

c:python ex8.py
1 2 3 4
'one' 'two' 'three' 'four'
True False False True
'%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'
'I had this thing.' 'That you could type up right.' "But it didn't sing." 'So I said gpnndnight.'
PS C:\work> python ex8.py
1 2 3 4
'one' 'two' 'three' 'four'
True False False True
'%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'
'I had this thing.' 'That you could type up right.' "But it didn't sing." 'So I said goodnight.'
c:python ex8.py

#为什么最后一行有双引号和单引号，那个双引号是怎么来的？
原因是"But it didn't sing "中含有一个单引号（didn't)，所以python在输出时外面加了双引号。
    如果用单引号包含它，就成了'But it didn't sing.'。python会认为'But it didn'是个字符串，Python并不知道如何处理该行余下的内容。
这时可以在用\符号，加在单引号前面（didn\'t），Python就知道这是字符串的内容。

答案来源：https://www.tuziang.com/combat/2018.html
