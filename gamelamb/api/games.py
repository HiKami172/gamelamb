from flask import Blueprint
import json

games = Blueprint("games", __name__)


@games.route('/games')
def get_games():
    with open('gamelamb/games.json', 'r') as f:
        data = json.load(f)
        print(data)
    return data
