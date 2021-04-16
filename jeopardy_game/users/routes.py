from flask import render_template, Blueprint
from jeopardy_game.users.forms import RegistrationForm

users = Blueprint('users', __name__)

@users.route('/user/home')
def user_home():
    return render_template('user_home.html', title="User Homepage")

@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)