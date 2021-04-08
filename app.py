# -*- coding: utf-8 -*-
"""
2021-4-8

@author: 李运辰

公众号：python研究者
"""
import requests
import time
import json




from flask import Flask,render_template,request,Response,redirect,url_for
from flask_cors import CORS
#内网ip
app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
CORS(app, supports_credentials=True)


############################flask路由
#进入页面
@app.route('/')
def index():
    return render_template('index.html')

#
if __name__ == "__main__":
    """初始化,debug=True"""
    app.run(host='127.0.0.1', port=5000,debug=True)
