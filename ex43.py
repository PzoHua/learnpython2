#_*_coding=utf-8_*_

import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
      "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" :
      "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
      "class %%% has-a functon named *** that takes self and @@@ parameters.",
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***.***(@@@)":
      "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
      "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
PHRASES_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASES_FIRST = True
else:
    PHRASES_FIRST = False
    
# load up the words from the website    # 加载网站上的文字
for word in urlopen(WORD_URL).readlines():  # 将网页中的文字一行一行送给word
    WORDS.append(word.strip())  #.str()用于移除字符首尾字符，默认为空符


def convert(snippet, phrase):
# 将WORDS里面的单词随机排列后一个首字母大写赋给class_names
    class_names = [w.capitalize() for w in
                random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []
    
    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))
        
    for sentence in snippet, phrase:
        result = sentence[:]
        
        # fake other names
        for word in class_names:
            result = result.replace("%%%", word, 1)
            
        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)
            
        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)
        
        results.append(result)
    
    return results
    
# keep going until they hit CTRL-D
try:
    while True:
        snippets = PHRASES.keys()
        random.shuffle(snippets)
        
        for snippet in snippets:
            phrase = PHRASES[snippet]
            question,answer = convert(snippet,phrase)
            if PHRASES_FIRST:
                question,answer = answer, question
                
            print question
                
                
            raw_input("> ")
            print "ANSWER: %s\n\n" % answer
                
except EOFError:
    print "\nBye"
