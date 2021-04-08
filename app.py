from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title="Home")

@app.route('/browse_games')
def browse_games():
    return render_template('browse_games.html', title="Games")