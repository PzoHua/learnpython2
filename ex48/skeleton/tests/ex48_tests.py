#_*_coding=utf-8_*_

# 测试文件lexicon的代码

from nose.tools import *
from ex48 import lexicon

# 测试 lexicon文件中的 scan函数下 directions
# assert_equal(a, b)  核实 a==b 

def test_directions():

    assert_equal(lexicon.scan("north"), [('direction', 'north')])
    result = lexicon.scan("north south east west")
    assert_equal(result, [('direction', 'north'),
                        ('direction', 'south'),
                        ('direction', 'east'),
                        ('direction', 'west')])

# 测试 lexicon文件中的 scan函数中下 verbs
def test_verbs():

    assert_equal(lexicon.scan("go"), [('verb', 'go')])
    result = lexicon.scan("go kill eat stop")
    assert_equal(result, [('verb', 'go'),
                        ('verb', 'kill'),
                        ('verb', 'eat'),
                        ('verb', 'stop')])

# 测试 lexicon文件中的 scan函数下 stops
def test_stops():

    assert_equal(lexicon.scan("the"), [('stop', 'the')])
    result = lexicon.scan("the in of from at")
    assert_equal(result, [('stop', 'the'),
                        ('stop', 'in'),
                        ('stop', 'of'),
                        ('stop', 'from'),
                        ('stop', 'at')])

# 测试 lexicon文件中的 scan函数下 nouns
def test_nouns():

    assert_equal(lexicon.scan('bear'), [('noun', 'bear')])
    result = lexicon.scan("bear princess")
    assert_equal(result, [('noun', 'bear'),
                        ('noun', 'princess')])

# 测试 lexicon文件中的 scan函数下 number
def test_number():

    assert_equal(lexicon.scan('1234'), [('number', 1234)])
    result = lexicon.scan("3 91234")
    assert_equal(result, [('number', 3),
                        ('number', 91234)])
                   
# 测试 lexicon文件中的 scan函数下报错结构
def test_errors():
    
    assert_equal(lexicon.scan("ASDFADFASDF"), [('error', 'ASDFADFASDF')])
    result = lexicon.scan("bear IAS princess")
    assert_equal(result, [('noun', 'bear'),
                                    ('error', 'IAS'),
                                    ('noun', 'princess')])
