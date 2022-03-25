from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import mysql.connector

app = Flask(__name__)

# for login authentication using mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",database="localstore",port=3306)
cursor=conn.cursor()

#for making connection to our database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/localstore'
db=SQLAlchemy(app)

class Signup(db.Model):
    '''sno,username,email, contactno,password,date'''

    sno= db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20),  nullable=False)
    contactno = db.Column(db.String(12), nullable=False)
    password= db.Column(db.String(20), nullable=False)
    date = db.Column(db.String(12),  nullable=True)


@app.route('/')
def hello_world():
    return render_template('home1.html')

@app.route('/mainhome')
def mainhome():
    return render_template('mainhome.html')

@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method=='POST':
       # adding entry to our database

      name=request.form.get('name')
      email= request.form.get('email')
      contact=  request.form.get('contact')
      password= request.form.get('password')
      entry=Signup(username=name,email=email,contactno=contact,password=password,date=datetime.now())

      db.session.add(entry)
      db.session.commit()

    return render_template('signup.html')

@app.route('/signin',methods=['POST','GET'])
def signin():
 
    email=request.form.get('signin_email')
    password=request.form.get('signin_password')

    cursor.execute(""" SELECT * FROM `signup` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email,password))
    users=cursor.fetchall()
     
    if len(users)>0:
      return render_template('home1.html')
    else:
      return render_template('signup.html')
# connecting storesignup to db
class Stores(db.Model):
    '''sno,store-name,email, contact,address,password,daate'''

    sno= db.Column(db.Integer, primary_key=True)
    storename = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20),  nullable=False)
    contact = db.Column(db.String(12), nullable=False)
    address= db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(12),  nullable=True)
    date = db.Column(db.String(12),  nullable=True)
@app.route('/store_signup',methods=['GET','POST'])
def storesignup():
     if request.method=='POST':
       # adding entry to our database

      name=request.form.get('store_name')
      email= request.form.get('store_email')
      contact=  request.form.get('store_contact')
      address= request.form.get('store_address')
      password= request.form.get('store_password')
      entry=Stores(storename=name,email=email,contact=contact,address=address,password=password,date=datetime.now())

      db.session.add(entry)
      db.session.commit()
     return render_template('storesignup.html')
# dashboard login validaion
@app.route('/store_signin',methods=['POST','GET'])
def store_signin():
 
    email=request.form.get('store_email')
    password=request.form.get('store_password')

    cursor.execute(""" SELECT * FROM `stores` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email,password))
    
    users=cursor.fetchall()

    if len(users)>0:
      return render_template('dashboard.html',details=users)
    else:
      return render_template('storesignup.html')

if __name__ == '__main__':
    app.run(debug=True)
