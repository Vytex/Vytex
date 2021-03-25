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
#TODO either alter or remove bellow


#class RegisterForm(Form):
    #username = StringField('Username', [validators.Length(min=4, max=25)])
    #email  = StringField('Email', [validators.Length(min=6, max=50)])
    #password = PasswordField('Password', [
        #validators.DataRequired(),
        #validators.EqualTo('confirm', message='Passwords do not match')
    #])
    #confirm = PasswordField('Confirm Password')



#def register():
    #form = RegisterForm(request.form)
    #if request.method == 'POST' and form.validate():
        #return render_template('create.html')    
    #return render_template('create.html', form=form)
@authorization.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'GET':
        return render_template('Create/signup.html')
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    image_file = request.form.get('image2')

    user = User.query.filter_by(email=email).first()

    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    new_user = User(email=email, username=username, password=generate_password_hash(password, method='sha256'), image_file=image_file)

    db.session.add(new_user)
    db.session.commit()
    #return redirect(url_for('app.login'))
    #return create_controller.index()
    #return render_template('Create/signup.html')
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
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials

    #return login_controller.index()
    #return render_template('LogIn/index.html')
    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('auth.profile'))

@authorization.route('/profile', methods=['GET'])
@login_required
def profile():
    image_file= url_for('static', filename='assets/' + current_user.image_file)
    return render_template('Profile/profile.html', username=current_user.username, image_file=image_file)

@authorization.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@authorization.route('/userLines', methods=['GET'])
@login_required
def LineHistory():
    return render_template('userLines/index.html')
