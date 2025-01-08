from flask import request
from flask_socketio import Namespace, join_room, leave_room, rooms
from manager import create_conversation  # Import the API function
from app import app, socketio

class WebSocketHandler(Namespace):
    def __init__(self, namespace):
        super().__init__(namespace)

    def on_connect(self):
        print(f'Client connected with session ID: {request.sid}')

    def on_disconnect(self):
        print(f'Client disconnected with session ID: {request.sid}')

    def on_join_room(self, data):
        conversation_id = data.get('conversation_id')
        current_rooms = rooms()
        for room in current_rooms:
            if room != request.sid:  # Avoid leaving the default room
                leave_room(room)
                print(f'Client left room: {room}')
        join_room(conversation_id)
        print(f'Client joined room: {conversation_id}')

    def on_leave_room(self, data):
        conversation_id = data.get('conversation_id')
        leave_room(conversation_id)
        print(f'Client left room: {conversation_id}')

    def on_v1_conversation(self, data):
        conversation_id = data.get('conversation_id')
        message = data.get('message')

        # Directly call the create_conversation function
        data = {'conversation_id': conversation_id, 'message': message}
        response = create_conversation()

        # Emit the response back to the client
        socketio.emit('v1_conversation', response, room=conversation_id)


# Initialize SocketIO with the Flask app and eventlet mode
socketio.init_app(app, async_mode='eventlet')

# Register the namespace
socketio.on_namespace(WebSocketHandler('/conversation'))