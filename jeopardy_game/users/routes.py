from flask import render_template, Blueprint

users = Blueprint('users', __name__)

@users.route('/user/home')
def user_home():
    return render_template('user_home.html', title="User Homepage")