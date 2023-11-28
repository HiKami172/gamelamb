from .extensions import socketio
from .db import get_db
import uuid


def create_player(session_id: str, is_host: bool = False):
    player_id = uuid.uuid4()


@socketio.on("create-room")
def handle_create_room(data):
    game_url = data.get('game_url')
    room_name = data.get('room_name')
    db = get_db()

    db.execute(
        "INSERT INTO GameRooms (game_url, room_name) VALUES (?, ?)",
        (game_url, room_name)
    )
    db.commit()

    socketio.emit('room-created', {'status': 'ok'}, broadcast=False)


@socketio.on("join-room")
def handle_join_room(room_id):
    pass


@socketio.on("leave")
def handle_leave(data):
    room = data['room']
    user = data['user']
