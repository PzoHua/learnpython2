#_*_coding=utf-8_*_

# 测试专用的骨架文件
from nose.tools import *
import NAME

def setup():
	print "SETUP!"
	
def teardown():
	print "TEAR DOWN!"

def test_basic():
	print "I RUN!"
