from flask import Flask
from flask import *
import bd
import sqlite3
from flask import render_template
import quires


app = Flask(__name__)
HOST = '127.0.0.1'
PORT = 8080

mybd = sqlite3.connect('users.db', check_same_thread=False)

nic = ''
age = 0

def add_user(username: str, age: int) -> bool:
    return True

def get_user_age(username: str) -> int:
    return 

def create_db():
    pass

def create_table():
    pass

@app.route('/user', methods=['POST', 'GET'])
def user():
    if request.method == 'GET':
        return '''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport"
                            content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
                            integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
                            crossorigin="anonymous">
                            <title>Регистрация</title>
                          </head>
                          <body>
                            <h1>Вы не зарегистрированы в системе Бонча!</h1>
                            <form method="post">
                              <div class="form-group">
                              <div class="form-group col-md-5">
                                <label for="nic">Имя</label>
                                <input type="text" class="form-control" id="nic" aria-describedby="emailHelp" placeholder="Введите Ваше имя" name="nic">
                              </div>
                              <div class="form-group">
                                <div class="form-group col-md-5">
                                  <label for="classSelect">Возраст</label>
                                  <input type="int" class="form-control" id="age" aria-describedby="emailHelp" placeholder="Введите Ваш возраст" name="age">
                                </div>
                              </div>
                              <button type="submit" class="btn btn-outline-success col-md-2">Регистрация</button>
                            </form>
                            </form>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        nic = request.form['nic']
        age = request.form['age']
        quires.add_user(nic,  age)
        print(nic, age)
    #return redirect('/get_age')
    return nic, age

@app.route('/get_age', methods=['GET'])
def get_age():
    user = request.args.get('nic')
    uage = quires.get_user_age(user)
    return str(uage)

if __name__ == '__main__':
    quires.create_db()
    quires.create_table('main')
    app.run(port=PORT, host=HOST)