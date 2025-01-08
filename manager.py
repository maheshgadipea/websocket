
def create_conversation(data):
    # Emit an event to the WebSocket clients
    conversation_id = data.get('conversation_id')

    # Process the data as needed
    response = {"status": "success", "data": data,
                "conversation_id": conversation_id}

    return  response