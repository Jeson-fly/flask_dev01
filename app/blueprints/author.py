# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：993811091@qq.com
  Time  ：2023/3/22
  Desc  ：
"""

from flask import Blueprint

author = Blueprint("author", __name__)


@author.route("/index")
def index():
    return "hello author"
