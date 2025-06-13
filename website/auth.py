from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from .models import User
from . import db

auth = Blueprint('auth', __name__)

class AuthService:
    """Handles authentication logic. SOLID principle: Single Responsibility Principle (SRP)"""


    @staticmethod
    def authenticate(username, password):
        user = User.query.filter_by(username=username).first()
        if not user:
            return None, 'Username does not exist.'
        if not check_password_hash(user.password, password):
            return None, 'Incorrect password, try again.'
        return user, None

    @staticmethod
    def register(username, first_name, password1, password2):
        if User.query.filter_by(username=username).first():
            return None, 'Username already exists.'
        if password1 != password2:
            return None, 'Passwords do not match.'
        if len(username) < 3 or len(password1) < 3:
            return None, 'Username and password must be at least 3 characters.'
        new_user = User(
            username=username,
            first_name=first_name,
            password=generate_password_hash(password1, method='pbkdf2:sha1', salt_length=8)
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user, None


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if not username or not password:
            flash('Username and password are required.', category='error')
            return render_template('login.html', user=current_user), 400
        user, error = AuthService.authenticate(username, password)
        if user:
            login_user(user, remember=True)
            flash('Logged in successfully!', category='success')
            return redirect(url_for('routes.home'))
        else:
            flash(error, category='error')
            return render_template('login.html', user=current_user), 401
    return render_template('login.html', user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', category='success')
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        first_name = request.form.get('first_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user, error = AuthService.register(username, first_name, password1, password2)
        if user:
            flash('Account created!', category='success')
            login_user(user, remember=True)
            return redirect(url_for('routes.home'))
        else:
            flash(error, category='error')
            return render_template('sign-up.html', user=current_user), 400
    return render_template('sign-up.html', user=current_user)
