# @Time    : 2020/10/24 下午1:52

__author__ = 'xhb'


from flask import Blueprint, url_for, render_template,\
    redirect, make_response, request, jsonify,current_app
import json
from datetime import datetime, timedelta


web = Blueprint('web', __name__, template_folder='templates')


from app.web import password
from app.web import short_url