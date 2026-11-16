from flask import Flask,render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/addCard')
def addCard():
    return render_template("addCard.html")

@app.route('/sendOtp')
def sendOtp():
    return render_template("sendOtp.html")

@app.route('/revise')
def revise():
    return render_template("revise.html")





if __name__== '__main__':
    app.run(debug=True)