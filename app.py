from flask import Flask, request, jsonify
from flask_socketio import SocketIO
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

# Initialize SocketIO
socketio = SocketIO(app, message_queue=os.getenv('RABBITMQ_URL'))