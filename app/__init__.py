# -*- coding: utf-8 -*-
# @Time    : 2020/10/23 16:35
# @Author  : xhb
# @FileName: __init__.py.py
# @Software: PyCharm


from app.models import db
from flask_login import LoginManager
from flask import Flask
from flask_mail import Mail


login_manager = LoginManager()
# mail = Mail()


def register_web_blueprint(app):
    from app.web import web
    app.register_blueprint(web)


def create_app():
    app = Flask(__name__)

    #: load default configuration
    app.config.from_object('app.setting')
    app.config.from_object('app.secure')

    # 注册login 模块
    # login_manager.init_app(app)
    # login_manager.login_view = 'web.login'
    # login_manager.login_message = '请先登录或注册'

    # 注册SQLAlchemy
    db.init_app(app)

    # mail.init_app(app)

    # register_api_blueprint(app)
    register_web_blueprint(app)

    return app
