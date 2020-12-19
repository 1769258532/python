#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

import pytest
@pytest.fixture()
def  login_fixture():

    print("--登录")

    yield

    print("---推出")


def test_order(login_fixture):
    print("token ===" , login_fixture)
    print("---下单业务执行的测试逻辑-----------------")
    assert 1