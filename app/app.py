#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz

#Flaskオブジェクトの生成
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///realestate.db'
db = SQLAlchemy(app)
#   __tablename__ = 'questions'

class AskQuestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(10),nullable=False)
    genre = db.Column(db.String(20), nullable=False)
    body = db.Column(db.Text(2000), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.now(pytz.timezone('Asia/Tokyo')))


#「/」へアクセスがあった場合に、"Hello World"の文字列を返す
#@app.route("/")
#def hello():
#    return "Hello World"

#@app.route("/index/<city>")
#def ccc(city):
#    return render_template("index.html", city=city)

#「/index」へアクセスがあった場合に、「index.html」を返す
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        genre = request.form.get('genre')
        body = request.form.get('body')
        askQuestion = AskQuestion(nickname=name, genre=genre, body=body)
        db.session.add(askQuestion)
        db.session.commit()
        return render_template('questions.html')
    else:
        return render_template("index.html")

@app.route("/questions", methods=['GET', 'POST'])
def questions():
    if request.method == 'GET':
        askQuestion = AskQuestion.query.all() 
        return render_template("questions.html", askQuestion=askQuestion)

@app.route("/answerers")
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

@app.route("/register_user")
def register_user():
    return render_template("register_user.html")



#おまじない
if __name__ == "__main__":
    app.run(debug=True)