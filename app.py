from flask import Flask, render_template, request, redirect, session
import mysql.connector
# from sentiments import second
import os
from app2 import second

app = Flask(__name__)

# initializing the user cookie
app.secret_key = os.urandom(24)

# blueprint to call the second file in the project
app.register_blueprint(second)

# establishing a connection with mysql database made in the xampp

cursor = None
print(type(session))
try:
    conn = mysql.connector.connect(
        host="LongTran", user="tlt834", password="aet5gnkaet7apct", database="my_database"
    )
    cursor = conn.cursor()
    print("Database connection successful.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    conn = None

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/home')
def home():
    if 'user_id' in session:
        return render_template('home.html')
    else:
        print(session)
        return redirect('/')
    
@app.route('/login_validation', methods = ['POST'])
def login_validation():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    print(email)
    print("SELECT * FROM users WHERE email = '{}' and password = '{}'".format(email, password))

    cursor.execute(
    "SELECT * FROM users WHERE email = '{}' and password = '{}'".format(email, password))

    users = cursor.fetchall()
    print(users)
    if len(users) > 0:
        session['user_id'] = users[0][0]
        print(users[0][0])
        print(session['user_id'])
        return redirect('/home')
    else:
        return redirect('/login')
    
@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form.get('uname')
    email = request.form.get('uemail')
    password = request.form.get('upassword')

    # Use parameterized query to prevent SQL injection
    cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", (name, email, password))
    conn.commit()  # Commit the changes to the database

    # Retrieve the user data based on the email
    cursor.execute("SELECT * FROM users WHERE email LIKE %s", (email,))
    myuser = cursor.fetchall()

    # Check if user data was retrieved
    if myuser:
        session['user_id'] = myuser[0][0]  # Assign user_id from the first result
        return redirect('/home')
    else:
        return "Error: User not found after registration. Please try again.", 400

@app.route('/logout')
def logout():
    session.pop('user_id')
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)