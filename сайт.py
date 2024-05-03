from flask import Flask
from flask import *
import bd
import sqlite3
from flask import render_template


app = Flask(__name__)
HOST = '127.0.0.1'
PORT = 8080

mybd = sqlite3.connect('users.db', check_same_thread=False)

nic = ''


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
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
                            <h1>Вы не зарегистрированы в системе КиноКрит!</h1>
                            <form method="post">
                              <div class="form-group">
                                <div class="form-group col-md-5">
                                  <label for="inputEmail4">Email</label>
                                  <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                </div>
                                <div class="form-group col-md-5">
                                  <label for="inputPassword4">Password</label>
                                  <input type="password" class="form-control" id="password" placeholder="Введите пароль" name="password">
                                </div>
                              </div>
                              <div class="form-group col-md-5">
                                <label for="nic">Nic</label>
                                <input type="text" class="form-control" id="nic" aria-describedby="emailHelp" placeholder="Введите Ваш ник" name="nic">
                              </div>
                              <div class="form-group">
                                <div class="form-group col-md-5">
                                    <label for="about">Немного о себе</label>
                                    <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                </div>
                                <div class="form-group col-md-4">
                                  <label for="classSelect">Возраст</label>
                                  <select id="classSelect" class="form-control">
                                    <option selected>Меньше 14</option>
                                    <option>14</option>
                                    <option>15</option>
                                    <option>16</option>
                                    <option>17</option>
                                    <option>18</option>
                                    <option>Больше 18</option>
                                  </select>
                                </div>
                              </div>
                              <div class="form-group col-md-5">
                                    <label for="form-check">Укажите пол</label>
                                    <div class="form-check">
                                      <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                      <label class="form-check-label" for="male">
                                        Мужской
                                      </label>
                                    </div>
                                    <div class="form-check">
                                      <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                      <label class="form-check-label" for="female">
                                        Женский
                                      </label>
                                    </div>
                              </div>
                              <button type="submit" class="btn btn-outline-success col-md-2">Регистрация</button>
                            </form>
                            </form>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        global nic
        nic = request.form['nic']

        user.insert(request.form['nic'], request.form['password'],
                    request.form['class'], request.form['email'], request.form['sex'])

        return redirect('/profile/' + request.form['nic'])