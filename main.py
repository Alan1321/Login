from flask import Flask, render_template, request,redirect
from flask_mysqldb import MySQL
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password123",
    database = "logininfo"
)
cur = mydb.cursor()

@app.route('/', methods = ['GET','POST'])
def index():
    print("im in index function")
    cur.execute("SELECT * FROM table1")
    result = cur.fetchall()
    if request.method == 'POST':
        if True:
            print("im in index redirecting to welcome html")
            return redirect('welcome.html')
    return render_template('index.html', result = result)

@app.route('/register.html', methods = ['GET','POST'])
def register():
    cur.execute("SELECT * FROM table1")
    result = cur.fetchall()
    print("im in register function")
    if request.method == 'POST':
        print("im in register redirecting to complete.html")
        userDetails = request.form
        lastname = userDetails['lastname']
        firstname = userDetails['firstname']
        username = userDetails['username']
        password = userDetails['password']
        cur.execute("INSERT INTO table1(lastname,firstname, username, password) VALUES(%s, %s,%s,%s)", 
        (lastname,firstname,username, password))
        mydb.commit()
        return redirect('complete.html')
    return render_template('register.html', result = result)

@app.route('/welcome.html')
def welcome():
    print("im in welcome function")
    return render_template('welcome.html')

@app.route('/complete.html')
def complete():
    print("im in complete function")
    return render_template('complete.html')

@app.route('/index.html')
def index2():
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

