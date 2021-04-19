from flask import render_template, Blueprint, flash, redirect, url_for
from jeopardy_game.users.forms import RegistrationForm, LoginForm

users = Blueprint('users', __name__)

@users.route('/user/home')
def user_home():
    return render_template('user_home.html', title="User Homepage")

@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account created!', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)

@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Welcome back!', 'success')
        return redirect(url_for('main.home'))
    return render_template('login.html', title='Login', form=form)