from flask import request
from abc import ABC, abstractmethod
from flask_socketio import Namespace, join_room, leave_room, rooms
from manager import create_conversation  # Import the API function

class AbstractSocketHandler(ABC, Namespace):
    def __init__(self, namespace, socketio):
        super().__init__(namespace)
        self.socketio = socketio

    @abstractmethod
    def on_connect(self):
        pass

    @abstractmethod
    def on_disconnect(self):
        pass

    @abstractmethod
    def on_conversation(self, data):
        pass

    @abstractmethod
    def on_join_room(self, data):
        pass

    @abstractmethod
    def on_leave_room(self, data):
        pass

    @abstractmethod
    def on_question(self, data):
        # Call the required function and provide the emit function
        # test_function(data, self.emit)
        pass

class ConversationSocketHandler(Namespace):
    def __init__(self, namespace, socket):
        super().__init__(namespace)
        self.socketio = socket

    def on_connect(self):
        print(f'Client connected with session ID: {request.sid}')

    def on_disconnect(self):
        print(f'Client disconnected with session ID: {request.sid}')

    def on_join_conversation(self, data):
        conversation_id = data.get('conversation_id')
        current_rooms = rooms()
        for room in current_rooms:
            if room != request.sid:  # Avoid leaving the default room
                leave_room(room)
                print(f'Client left room: {room}')
        join_room(conversation_id)
        print(f'Client joined room: {conversation_id}')

    def on_leave_conversation(self, data):
        conversation_id = data.get('conversation_id')
        leave_room(conversation_id)
        print(f'Client left room: {conversation_id}')

    def on_question(self, data):
        conversation_id = data.get('conversation_id')
        message = data.get('question')
        print(f"Currently inside question function with id is : {conversation_id}")

        # call the create_conversation function and always provide the emit function
        data = {'conversation_id': conversation_id, 'message': message}
        response = create_conversation(data,self.emit)

        # Emit the response back to the client
        self.emit('answer', {'answer': response, 'conversation_id': conversation_id}, room=conversation_id)

