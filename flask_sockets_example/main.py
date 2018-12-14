from flask import Flask, render_template
from flask_socketio import SocketIO, emit


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect_event', namespace='/test')
def connect_event(payload):
    print("Client connected.")
    emit('response_event', {
        'data': 'Connected'
    })

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

@socketio.on('single_event', namespace='/test')
def my_event(payload):
    print("Received:", payload['data'])
    emit('response_event', {
        'data': payload['data'],
    })

@socketio.on('broadcast event', namespace='/test')
def broadcast_event(payload):
    print("Received:", payload['data'])
    emit('response_event', {
        'data': payload['data'],
    }, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
