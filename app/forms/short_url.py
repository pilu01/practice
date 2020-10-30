# -*- coding: utf-8 -*-
# @Time    : 2020/10/30 9:58
# @Author  : xhb
# @FileName: short_url.py
# @Software: PyCharm


from wtforms import StringField, IntegerField, Form, PasswordField, SubmitField
from wtforms.validators import Length, NumberRange, DataRequired, length, Email, ValidationError, EqualTo, URL
from flask_wtf import FlaskForm


class UrlForm(FlaskForm):
    url = StringField(u'url', validators=[DataRequired(), URL(message='url地址不符合规范')])
    submit = SubmitField(u'提交')

