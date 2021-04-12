from flask import Flask
from jeopardy_game.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from jeopardy_game.main.routes import main
    from jeopardy_game.users.routes import users
    app.register_blueprint(main)
    app.register_blueprint(users)

    return app