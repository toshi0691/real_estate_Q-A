#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin,LoginManager, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
import pytz
import sqlite3
import copy
import os


#Flaskオブジェクトの生成
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///realestate.db'
app.config['SECRET_KEY'] = os.urandom(24)
#app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
#   __tablename__ = 'questions'

class AskQuestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(10), nullable=False)
    genre = db.Column(db.String(20), nullable=False)
    body = db.Column(db.Text(2000), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.now(pytz.timezone('Asia/Tokyo')))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_kannji = db.Column(db.String(10), nullable=False)
    name_hiragana = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    birthday = db.Column(db.Integer, primary_key=True)
    postcode = db.Column(db.Integer, nullable=False)
    address_pref = db.Column(db.String(4), nullable=False)
    address_city = db.Column(db.String(60), nullable=False)
    #address_number = db.Column(db.String(20), nullable=False)
    address_building = db.Column(db.String(50), nullable=False)
    e_mail = db.Column(db.String(70), nullable=False)
    login_id = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(15), nullable=False)
    password_confirm = db.Column(db.String(15), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    policy_confirm = db.Column(db.String(2), nullable=False)

# db.create_all()

#「/」へアクセスがあった場合に、"Hello World"の文字列を返す
#@app.route("/")
#def hello():
#    return "Hello World"

#@app.route("/index/<city>")
#def ccc(city):
#    return render_template("index.html", city=city)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/", methods=['GET', 'POST'])
def index():
    if  request.method == 'POST':
        name = request.form.get('name')
        genre = request.form.get('genre')
        body = request.form.get('body')
        askQuestion = AskQuestion(nickname=name, genre=genre, body=body)
        askQuestion_copy = copy.deepcopy(askQuestion)
        db.session.add(askQuestion)
        db.session.commit()
        return render_template('questions.html', askQuestion=askQuestion_copy)
    else:
        return render_template("index.html")

@app.route("/questions", methods=['GET', 'POST'])
def questions():
    if  request.method == 'GET':
        askQuestion = AskQuestion.query.all() 
        return render_template("questions.html", askQuestion=askQuestion)

@app.route("/answerers")
@login_required
def answerers():
    return render_template("answerers.html")

@app.route("/choose_membership_type")
def choose_membership_type():
    return render_template("choose_membership_type.html")

@app.route("/privacypolicy")
def privacypolicy():
    return render_template("privacypolicy.html")

@app.route("/register_answerer")
def register_answerer():
    return render_template("register_answerer.html")

@app.route("/register_user", methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        name_kannji = request.form.get('username_kannji')
        name_hiragana = request.form.get('username_hiragana')
        gender = request.form.get('gender')
        birthday = request.form.get('birthday')
        postcode = request.form.get('postcode')
        address_pref = request.form.get('pref2')
        address_city = request.form.get('address_city')
        address_building = request.form.get('address_building')
        e_mail = request.form.get('e_mail')
        login_id = request.form.get('login_id')
        password = request.form.get('password')
        password_confirm = request.form.get('password_confirm')
        phone_number = request.form.get('phone_number')
        policy_confirm = request.form.get('agree_policy')
        user = User(name_kannji=name_kannji, name_hiragana=name_hiragana, gender=gender, birthday=birthday, postcode=postcode,\
        address_pref=address_pref, address_city=address_city, address_building=address_building, e_mail=e_mail,\
        login_id=login_id, password=generate_password_hash(password, method='sha256'),\
        password_confirm=generate_password_hash(password_confirm, method='sha256'), phone_number=phone_number, policy_confirm=policy_confirm)
        user_copy = copy.deepcopy(user)
        db.session.add(user)
        db.session.commit()
        return redirect('login.html')
    else:
        return render_template("register_user.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = User.query.filter_by(username=username).first()
        if check_password_hash(user.password, password):
            login_user(user)
            return redirect('/')
        #例外処理必要
    else:
        return render_template('login.html')

@app.route('/logout')
@login_required #←loginしているユーザしかこの以下はアクセスできなくなるという書き方
def logout():
    logout_user()
    return redirect('/login')

#おまじない
if __name__ == "__main__":
    app.run(debug=True)