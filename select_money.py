#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@File ：select_money.py
@Auth ： luoluo
@Time ： 2021-02-18 17:20:57
@Description：
"""

# 定义工资查询方法
from python_deposit import money, send_money


def select_money():
    totle_money = money.saved_money() + send_money.send_money()
    # print(f'查询到工资数额为 {totle_money} 元')
    return totle_money


if __name__ == '__main__':
    print(select_money())
