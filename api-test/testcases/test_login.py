# -*- coding:utf-8 -*-
# @Emoj: （￣︶￣）↗　
# @Time: 2022/8/20 9:46
# @Author: wangxi
# @Email: 674860357@qq.com
# @File: test_login.py
# @Description:
import pytest

@pytest.fixture(params=['str'])
def hello(request) :
    return request.param

class TestLogin:
    @pytest.fixture(params=['password'])
    def test_password(self, request):
        print("hello, world ! ! !", request.param)
        return "1234"

    @pytest.fixture()
    def test_username(self):
        print("hello, world ! ! ! wangxi")
        return "wangxi"

    def test_submit(self, test_username, test_password):
        print("hello, world ! ! ! test_submit", test_password, test_username)

    def test_dismiss(self):
        print("hello, world ! ! ! dismiss")

    def test_code(self, hello):
        print("hello, world ! ! !", hello)

