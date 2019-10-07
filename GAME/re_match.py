#_*_coding=utf-8_*_
# 练习正则表达式 re.match()
# re.match()  从字符串起始位置处开始匹配，如果不成功，就返回None
# 匹配成功返回什么？ 返回结果位置re_match.py

# 函数语法 re.match(pattern, string, flags = 0)
""" pattern  匹配的正则表达式（最需要理解的）
    string   内容（好像要是字符串才行）
    flags    标志位（匹配的说明）；如是否区分大小写，多行匹配？？
"""
# re 应该是个函数库，类或者其他
import re

result1 = re.match(r'pu', 'puzhonghua')
result2 = re.match(r'zhong', 'puzhonghua')

print "result1: %s" % result1
print "result2: %s" % result2

运行结果：
-------------------------------------------------
PS C:\work> python .\test.py
result1: <_sre.SRE_Match object at 0x02A0FA68>
result2: None
PS C:\work>
-------------------------------------------------
