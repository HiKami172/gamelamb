import os

from flask import Flask
from flask_cors import CORS
from .events import socketio
from gamelamb.api .games import games
from gamelamb.api .main import main
from .db import init_app


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'gamelamb.sqlite'),
    )
    # db init
    init_app(app)
    # register blueprints
    app.register_blueprint(games)
    app.register_blueprint(main)
    # init socketio events
    socketio.init_app(app)

    return app
