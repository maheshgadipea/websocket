from flask import Flask, request, jsonify
from flask_socketio import SocketIO
import os
from flask import Flask, render_template, request, jsonify, session
from websocket import WebSocketHandler

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True


socketio = SocketIO(app, message_queue=os.getenv('RABBITMQ_URL'), cors_allowed_origins="*",async_mode='eventlet')

# Register the namespace
socketio.on_namespace(WebSocketHandler('/conversation', socketio))

@app.route('/')
def index():
    return render_template('index.html')