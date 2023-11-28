import sqlite3

import click
from flask import current_app, g
import json


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(init_games_command)


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES,
        )
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def execute_script(path: str):
    db = get_db()
    with current_app.open_resource(path) as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    execute_script('../scripts\\schema.sql')
    click.echo('Initialized the database.')


@click.command('init-games')
def init_games_command():
    """Reinitialize the list of games."""
    db = get_db()
    with open('games.json', 'r') as f:
        games = json.load(f)
    for game in games:
        attrs = games[game]
        data = (
            game,
            attrs['title'],
            attrs['description'],
            attrs['min_players'],
            attrs['max_players']
        )
        print(data)
        db.execute(
            "INSERT INTO games (url, title, description, min_players, max_players) VALUES (?, ?, ?, ?, ?)",
            data
        )
        db.commit()
    click.echo('Initialized the games.')
