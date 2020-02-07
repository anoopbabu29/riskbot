from flask import Flask, send_from_directory 
from flask_socketio import SocketIO, send, emit, join_room, leave_room
from typing import Dict, List, Any

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route('/<path:path>', methods=['GET'])
def static_proxy(path):
  return send_from_directory('./dist/risk-ui', path)


@app.route('/')
def root():
  return send_from_directory('./dist/risk-ui', 'index.html')


@app.errorhandler(500)
def server_error(e):
  return 'An internal error occurred [main.py] %s' % e, 500


@socketio.on('test')
def test(data):
    print('hi')
    emit('test_response', None)

'''
ROOM MANAGEMENT
'''
# Admin Creates the room
@socketio.on('create_room')
def on_create_room(data: Dict[str, Any]):
    room: str = f'{data["roomCode"]}{data["pass"]}'
    print(room)


# New Player Requests a Room
@socketio.on('req_room')
def on_req(data: Dict[str, Any]):
    print(data)
    room: str = f'{data["roomCode"]}{data["pass"]}'

    print(room)
    print(f'new_player_admin_{room}')

    emit(f'new_player_admin_{room}', {"name":data['name']}, json=True, broadcast=True)


# Admin checks whether the room is open or closed
@socketio.on('check_room')
def on_update(data: Dict[str, Any]):
    room: str = f'{data["roomCode"]}{data["pass"]}'
    can_join: bool = data['has_started']

    print(can_join)
    print(f'cpn_{room}')
    
    emit(f'cpn_{room}', {"can_join": can_join}, json=True, broadcast=True)


# Requect player info from Admin
@socketio.on('req_playerInfo')
def req_plinfo(data: Dict[str, Any]):
    room: str = f'{data["roomCode"]}{data["pass"]}'
    
    emit(f'upd_pl_rm_admin_{room}', None, broadcast=True)


# Admin sends everyone the updated list
@socketio.on('update_room')
def update_room(data: Dict[str, Any]):
    room: str = f'{data["roomCode"]}{data["pass"]}'
    player_list: List[str] = data['players']

    emit(f'update_list_{room}', {"players": player_list}, json=True, broadcast=True)


# Leave Room
@socketio.on('leave_room')
def on_leave(data: Dict[str, Any]):
    room: str = f'{data["roomCode"]}{data["pass"]}'

    emit(f'left_room_{room}', None)


if __name__ == '__main__':
    socketio.run(app)

