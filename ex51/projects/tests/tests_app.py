#_*_coding=utf-8_*_
from nose.tools import *
from bin.app import app
from tests.tools import assert_response

def test_index():
    # check that we get a 404 on the / URL
    resp = app.request("/")
    assert_response(resp, status="404")
    
    # test our first GET request to /hello
    resp = app.request("/hello")
    assert_response(resp)
    
    # make sure default value work for the form
    resp = app.request("/hello", method="POST")

    assert_response(resp, contains="Nobody")
    
    # test that we get expected value
    data = {'name': 'Zed', 'greet': 'Hola'}
    resp = app.request("/hello", method="POST", data=data)
    assert_response(resp, contains="Zed")


# 1.把调用的 app.response 得到的响应;
# 2.传递给 assert_response 函数，然后将要检查的内容作为参数传递给
#   assert_response 中的判断条件;
