#_*_coding=utf-8_*_

# 用assert断言函数，测试 parser.py程序
# 需要测试 peek

from nose.tools import *
from ex49 import parser
from ex49 import lexicon

sentence = "open the door"
word_list = lexicon.scan(sentence)
word_type = 'verb'

def test_peek():

    assert_equal(parser.peek(word_list), word_type)

def test_match():
    
    assert_equal(parser.match(word_list, word_type), ('verb', 'open'))
    
def test_parse_verb():
    
    assert_equal(parser.parse_verb(word_list), 'test')
    
def test_parse_object():
    
    assert_equal(parser.parse_object(word_list), ('noun', 'door'))

def test_parse_subject():
    
    assert_equal(parser.parse_subject(word_list), 'test')

def test_parse_sentence():
    
    assert_equal(parser.parse_sentence(word_list), '')
