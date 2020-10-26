# @Time    : 2020/10/25 上午10:47

__author__ = 'xhb'


from app.web import *


@web.route('/password', methods=['GET', 'POST'])
def password():
    if request.method == "POST":
        data = request.form.to_dict()
        password = data.get('password')
        salt = data.get('salt')
        length = int(data.get('length'))
        res = hash_password(password, salt, length)
        return jsonify({
            'text': res,
            'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
    return render_template('password/index.html')


@web.route('/test', methods=['GET', 'POST'])
def ces():
    if request.method == "POST":
        d = request.form.to_dict()
        v1 = d.get("v1")
        v2 = d.get("v2")
        res = int(v1) + int(v2)
        return jsonify(res)
    return render_template('password/test.html')


def hash_password(password, salt, len):
    import hashlib
    s = hashlib.sha256(password.encode('utf-8'))
    pwd = s.hexdigest()
    new_p = hashlib.sha256((pwd + salt).encode('utf-8'))

    return new_p.hexdigest()[:len]