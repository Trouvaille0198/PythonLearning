from flask import Flask, request, jsonify, abort, redirect, session

app = Flask(__name__)
app.secret_key = '123'


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/hello/<anything>')
def hello_anything(anything):
    return 'Hello %s' % anything


@app.route('/plus/<int:number>')
def wow_number(number):
    return '%s plus %s is %s' % (number, number, (number+number))


@app.route('/json/<string:data>')
def json(data):
    return {'data': data}


@app.route('/try/login', methods=['GET', 'POST'])
def try_login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()


@app.route('/bilibili')
def index():
    return redirect("https://www.bilibili.com")


@app.route('/test/post', methods=['POST'])
def post():
    print('gooooooood')
    my_json = request.get_json()
    print(my_json)
    name = my_json.get('name')+u'大帅哥'
    age = my_json.get('age')
    if all([name, age]):
        # return my_json.get('name') + ' is ' + str(my_json.get('age')) + ' years old.'
        return jsonify(name=name, age=age)
    else:
        return "Request failed!"


@app.route('/cookies')
def get_cookies():
    # 获取cookies
    return request.cookies


@app.route('/login', methods=["POST"])
def login():
    """
    登录
    :return: 
    """
    data = request.get_json()
    username = data.get('username')
    passwrd = data.get('passwrd')
    if not all([username, passwrd]):
        return jsonify('传输不完整!')
    if username == 'sun' and passwrd == '123':
        # 保存登陆状态在session中
        session['username'] = username
        session['passwrd'] = passwrd
        return jsonify(msg='Login successfully!')
    else:
        return jsonify(msg='Login failed!')


@app.route('/logout', methods=["GET"])
def logout():
    """
    退出登录
    """
    session.clear()
    return jsonify(msg='Logout!')


# app.run(debug=True)
app.run(debug=True)
