

def create_conversation(data,socket_emit):
    # Emit an event to the WebSocket clients
    conversation_id = data.get('conversation_id')
    print(f"conversation in create_conversation is : {conversation_id}")

    # Process the data as needed
    response = {"status": "success", "data": data,
                "conversation_id": conversation_id}
    
    socket_emit('answer', {'answer': "In progress", 'conversation_id': conversation_id}, room=conversation_id)
    import time
    time.sleep(5)
    return  str(response)


def test_task(socketio_instance):
    print("Background task started")
    a = 0
    while a < 6:
        print(f"My count is {a}")
        socketio_instance.sleep(3)
        a += 1
