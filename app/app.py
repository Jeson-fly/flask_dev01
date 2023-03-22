# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：993811091@qq.com
  Time  ：2023/3/22
  Desc  ：
"""

from flask import Flask
from blueprints.author import author

app = Flask("my_flask_Server")


@app.route("/", methods=["GET"])
def index():
    return "hello world"


def register_blueprints(app_: Flask):
    app_.register_blueprint(author, url_prefix='/author')


register_blueprints(app)

if __name__ == '__main__':
    app.run(port=8080, debug=True)
