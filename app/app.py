#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask,render_template

#Flaskオブジェクトの生成
app = Flask(__name__)


#「/」へアクセスがあった場合に、"Hello World"の文字列を返す
@app.route("/")
def hello():
    return "Hello World"


#「/index」へアクセスがあった場合に、「index.html」を返す
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/questions")
def questions():
    return render_template("questions.html")

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