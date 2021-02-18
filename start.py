#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@File ：start.py
@Auth ： luoluo
@Time ： 2021-02-18 17:30:54
@Description：
"""
# 启动查询工资的方法
from python_deposit import select_money

if __name__ == '__main__':
    totle_money = select_money.select_money()
    print(f'查询到最终存款有 {totle_money} 元')
