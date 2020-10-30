# @Time    : 2020/10/24 下午1:52

__author__ = 'xhb'


from flask import (Blueprint, url_for, render_template,
    redirect, make_response, request,
                   jsonify,current_app, flash)
import json
from datetime import datetime, timedelta
from app.models.short_url import ShortUrl
from app.models import db


web = Blueprint('web', __name__, template_folder='templates')


from app.web import password
from app.web import short_url