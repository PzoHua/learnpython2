#-*-coding=utf-8-*-

#练习将函数import到Python中

#模组break_words用来拆分字符串
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

#模组sort_words用来排序字符串
def sort_words(words):
    """Sorts the words."""
    return sorted(words)

#模组print_first_word用来输出首字符串
def print_first_word(words):
    """Print the first word after popping it off."""
    word = words.pop(0)
    print word

#模组print_last_word用来输出末尾字符串
def print_last_word(words):
    "Print the last word after popping it off."""
    word = words.pop(-1)
    print word

#模组sort_sentence用来拆分字符串并排序（通过调用模组break_words和模组sort_words)来实现
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words  = break_words(sentence)
    return sort_words(words)

#该模组调用break_words、print_first_word及print_last_word模组
#一次性实现三个模组的功能：拆分字符串、输出首字符串及末尾字符串
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

#该模组调用sort_sentence、print_first_word及print_last_word模组
#一次性现实三个模组功能：排序字符串、输出首尾字符串
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
	
以上是代码
----------------------------------------------------------------------------------------------------
--------------------------快乐的分割线---------------------------------------------------------------
----------------------------------------------------------------------------------------------------
以下是操作：该小程序将在python编译器里，用交互的方式和你的.py作交流
在终端运行python

PS C:\> python                                                                               
Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import ex25
>>> sentence = "All good things come to those who wait."
>>> words = ex25.break_words(sentence)
>>> words
['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
>>> sorted_words = ex25.sort_words(words)
>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
>>> ex25.print_first_word(words)
All
>>> ex25.print_last_word(words)
wait.
>>> wrods
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'wrods' is not defined
>>> words
['good', 'things', 'come', 'to', 'those', 'who']
>>> ex25.print_first_word(sorted_words)
All
>>> ex25.print_last_word(sorted_words)
who
>>> sorted_words
['come', 'good', 'things', 'those', 'to', 'wait.']
>>> sorted_words = ex25.sort_sentence(sentence)
>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
>>> ex25.print_first_and_last(sentence)
All
wait.
>>> ex25.print_first_and_last_sorted(sentence)
All
who
>>> ^Z

PS C:\>   
逐行分析每一步实现的功能：
第60行你将自己的ex25.py执行了import， 和你做过的其他import一样。在导入模组的时候不必.py加后缀名。
此时ex25.py被当作模组使用，里面的函数可以直接调用出来。

第61行创建了一个用来处理的“句子(entence)”。

第62行使用ex25调用定义的第一个函数 ex25.break_words。其中的 . (dot,period)符号用来告诉Python：
“嗨，我要运行 ex25 里的那个叫break_words的函数！”

第63行我们只输入了 words, 而python将在第64行打印出这个变量里的内容。看上去可能会觉得奇怪， 不过
这其实是一个“列表（list）”，在后面将学到它。

第65行调用ex25里的函数sort_words(words),并将处理过的值赋给 sorted_words;在67行输入sorted_words输出返回的值。

第68、70行分别调用了 ex25中定义的模组print_first_word及print_last_word,变量参数为words,在69、71行输出函数中的结果。

第72行我故意输出wrods，程序报错，说该变量名没有定义。

第76输入words，输出变量words中剩余的内容，可以看出首尾两个字符串已经不在了。

第78~81行调用ex25中的函数print_first_word及print_last_word，这次的变量参数为排序过的字符串（sorted_words)。

第82输入sorted_word,查看该变量中的剩余内容（第83行为输出结果）。

第84行通过ex25中定义的函数sort_sentence来处理“句子（sentence）”。

第87和90调用最后两个定义的函数，打印出相应的结果。

