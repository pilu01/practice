# -*- coding: utf-8 -*-
# @Time    : 2020/10/28 15:22
# @Author  : xhb
# @FileName: short_url.py
# @Software: PyCharm
from app.models import *


class ShortUrl(db.Model):
    __bind_key__ = 'kk'
    __tablename__ = 'short_url'
    id = db.Column(db.Integer, primary_key=True)
    short = db.Column(db.String(20), index=True)
    url = db.Column(db.String(2000))
    host = db.Column(db.String(20))
    create_time = db.Column(db.DateTime, default=datetime.now)
