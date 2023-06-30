from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

@app.route('/')
def sessions():
    return render_template('session.html')

@socketio.on('my event')
def handle_my_custom_event(data):
    user_name = data['user_name']
    message = data['message']
    message_data = {'user_name': user_name, 'message': message}
    emit('my response', message_data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
