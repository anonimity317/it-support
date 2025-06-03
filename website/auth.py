from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(f"Username: {username}, Password: {password}")
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return render_template('logout.html')

@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        # print(f"Username: {username}, First Name: {first_name}, Password1: {password1}, Password2: {password2}")

        # user = User.query.filter_by(username=username).first()
        # if user:
        #     flash('username already exists.', category='error')
        if len(username) < 5:
            flash('Username must be greater than 4 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 4:
            flash('Password must be at least 4 characters Long.', category='error')
        else:
            pass_out = generate_password_hash(password1,  method='pbkdf2:sha1', salt_length=8)
            new_user = User(username=username, first_name=first_name, password=pass_out, pu=False)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('routes.home'))
        
    return render_template('sign-up.html')