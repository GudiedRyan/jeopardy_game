from flask import render_template, Blueprint, redirect, url_for, flash, request

from jeopardy_game.games.forms import JeopardyForm

games = Blueprint('games', __name__)

@games.route('/create_game', methods=['GET', 'POST'])
def create_game():
    form = JeopardyForm()
    if form.validate_on_submit():
        flash('Game Created', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_game.html', title="New Game", form=form)