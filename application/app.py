from flask import Flask, request, jsonify
from flask_socketio import SocketIO
import os
from flask import Flask, render_template, request, jsonify, session
from websocket import ConversationSocketHandler
from manager import test_task

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True


socketio = SocketIO(app, message_queue=os.getenv('RABBITMQ_URL'), cors_allowed_origins="*",async_mode='eventlet')

# Register the namespace
socketio.on_namespace(ConversationSocketHandler('/conversation', socketio))

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/start-task', methods=['POST'])
def start_task():
    socketio.start_background_task(target=test_task, socketio_instance=socketio)
    return jsonify({"status": "Background task started"}), 200