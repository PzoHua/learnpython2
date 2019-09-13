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
	
	
