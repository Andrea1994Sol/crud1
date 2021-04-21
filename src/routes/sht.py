from src import app
from werkzeug.urls import url_parse
from flask_wtf import FlaskForm
from src.controllers.sht import ShortenController, UsersController, Authentication
from flask import make_response, session, jsonify, request, render_template, redirect, flash, url_for
import random, string, hashlib
from src.connection_bd.bd import mysql

shortenController = ShortenController()
usersController = UsersController()
authentication = Authentication()


@app.route('/urls', methods=['GET'])
def listUrls():
    urls = shortenController.listUrls()
    return render_template('sht/list.html', urls=urls)

    if session['user']:
        id = id;
        urls = shortenController.listUrlsUser(id)
        return render_template('sht/list.html', urls=urls)
        return session['user']
    else:
        return render_template('users/login.html', urls=urls)

@app.route('/shturl', methods=['POST'])
def createURL():
    url_to_shorten = request.form['url']

    if not url_to_shorten:
        flash('The URL is required!')
        return redirect(url_for('index.html'))

    letters = string.ascii_letters + string.digits
    f = 5
    url_show = 'localhost:3000/shturl/'
    url_content = ''
    for i in range(f):
        ramStr = random.choice(letters)
        url_content = url_content + ramStr
        url_show = url_show + ramStr

    url_shortened = url_content

    shortenController.generate_short_link(url_to_shorten, url_shortened)
    return render_template('sht/index.html', url_shortened=url_shortened, url_to_shorten=url_to_shorten, url_show=url_show)


@app.route('/shturl/<url_shortened>', methods=['GET'])
def redirectURL(url_shortened):
    data = shortenController.redirect_url(url_shortened)
    return redirect(data)

@app.route('/users', methods=['POST', 'GET'])
def createUser():
    user = request.form['user']
    email = request.form['email']
    passwordno = request.form['password']
    password = hashlib.md5(passwordno.encode())

    usersController.create_user(user, email, password.hexdigest())
    return render_template('users/create.html')
 
@app.route('/login', methods=['POST', 'GET'])
def loginUser():
    email = request.form['email']
    passwordno = request.form['password']
    passwordsn = hashlib.md5(passwordno.encode())
    password = passwordsn.hexdigest()

    userAuth = authentication.auth_user(email) 

    if userAuth and password == userAuth[1]:
        session['id'] = userAuth[3]
        session['user'] = userAuth[2]
        session['email'] = userAuth[0]
        success_message = 'Welcome {}'.format(userAuth[2])
        flash(success_message)
        return render_template('index.html',login=userAuth)
    else:
        error_message = 'User or password invalid!'
        flash(error_message)
        return render_template('users/login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return render_template("users/login.html")
