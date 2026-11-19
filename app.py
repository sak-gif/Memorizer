from flask import Flask,render_template,jsonify,request
import  sqlite3
app = Flask(__name__)
app.config['SECRET-KEY'] = 'sak-secret-key'

def get_db():
    conn = sqlite3.connect('memoriser.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')

init_db()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/api/register',methods=['GET','POST'])
def api_register():
    return jsonify(message="Registered"), 201

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register', methods=['Get'])
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