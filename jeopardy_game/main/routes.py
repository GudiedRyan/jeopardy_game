from flask import render_template, Blueprint

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home', methods=['GET'])
def home():
    return render_template('home.html', title="Home")

@main.route('/browse_games')
def browse_games():
    return render_template('browse_games.html', title="Games")