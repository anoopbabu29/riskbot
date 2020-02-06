from flask import Flask, send_from_directory 
from flask_socketio import SocketIO, send, emit, join_room, leave_room
from typing import Dict, List, Any

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/<path:path>', methods=['GET'])
def static_proxy(path):
  return send_from_directory('../risk-ui/dist/risk-ui', path)


@app.route('/')
def root():
  return send_from_directory('../risk-ui/dist/risk-ui', 'index.html')


@app.errorhandler(500)
def server_error(e):
  return 'An internal error occurred [main.py] %s' % e, 500


'''
ROOM MANAGEMENT
'''
# Admin Creates the room
@socketio.on('create_room')
def on_create_room(data: Dict[str, Any]):
    room: str = f'{data["roomCode"]}{data["pass"]}'
    
    join_room(room)


# New Player Requests a Room
@socketio.on('req_room')
def on_req(data: Dict[str, Any]):
    room: str = f'{data["roomCode"]}{data["pass"]}'
    
    emit('new_player_admin', data=None, include_self=False, room=room)


# Admin checks whether the room is open or closed
@socketio.on('check_room')
def on_update(data: Dict[str, Any]):
    room: str = f'{data["roomCode"]}{data["pass"]}'
    has_started: bool = data['has_started']

    emit('check_player_admin', data=has_started, include_self=False, room=room)


# Admin allows the room to be joined
@socketio.on('join_room')
def on_join(data: Dict[str, Any]):
    room: str = f'{data["roomCode"]}{data["pass"]}'
    name: str = data['name']
    
    join_room(room)

    emit('add_player_admin', data=name, include_self=False, room=room)


# Admin sends everyone the updated list
@socketio.on('update_room')
def update_room(data: Dict[str, Any]):
    room: str = f'{data["roomCode"]}{data["pass"]}'
    player_list: List[str] = data['players']

    emit('update_list', data=player_list, include_self=False, room=room)


# Leave Room
@socketio.on('leave_room')
def on_leave(data: Dict[str, Any]):
    room: str = f'{data["roomCode"]}{data["pass"]}'
    leave_room(room)

    emit('left_room', data=None, room=room)


if __name__ == '__main__':
    socketio.run(app)

