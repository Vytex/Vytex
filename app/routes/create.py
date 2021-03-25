from random import randint
import datetime
#from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user import User
from app.models.userSpot import Spot 
from app import db
from flask_login import login_user, login_required, current_user, logout_user

from flask import Blueprint, request, redirect, url_for,render_template, flash, session, logging

from app import app
from app.controller.create_controller import create_controller
authorization = Blueprint('auth',__name__)

@authorization.route('/signup', methods=['POST', 'GET'])
def signup():
    #sends user to signup page
    if request.method == 'GET':
        return render_template('Create/signup.html')
    #if 'POST' sends information to db
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    image_file = request.form.get('image2')

    user = User.query.filter_by(email=email).first()
    #reloads if email already exists
    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))
    #adds new user to db
    new_user = User(email=email, username=username, password=generate_password_hash(password, method='sha256'), image_file=image_file)

    db.session.add(new_user)
    db.session.commit()
    #sends user to login page after succesful signup
    return redirect(url_for('auth.login'))

@authorization.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('LogIn/index.html')
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        # if the user doesn't exist or password is wrong, reload the page
        return redirect(url_for('auth.login'))

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('auth.profile'))

@authorization.route('/profile', methods=['GET'])
@login_required
def profile():
    # displays profile picture if user logged in
    image_file= url_for('static', filename='assets/' + current_user.image_file)
    return render_template('Profile/profile.html', username=current_user.username, image_file=image_file)

@authorization.route('/logout')
@login_required
def logout():
    logout_user()
    #logs user out, terminates session
    return redirect(url_for('auth.login'))

@authorization.route('/userLines', methods=['GET'])
@login_required
def LineHistory():
    #returns user line after veryifying authorization
    return render_template('userLines/index.html')
