# @Time    : 2020/10/24 下午1:52

__author__ = 'xhb'


from flask import Blueprint, url_for, render_template, redirect, make_response


web = Blueprint('web', __name__, template_folder='templates')


from app.web import password