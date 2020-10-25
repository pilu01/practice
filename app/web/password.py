# @Time    : 2020/10/25 上午10:47

__author__ = 'xhb'


from app.web import *


@web.route('/password')
def password():
    return render_template('password/index.html')



