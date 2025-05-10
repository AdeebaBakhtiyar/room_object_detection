def simple_chatbot(detected_objects):
    if not detected_objects:
        return "I couldn't detect anything. Try again!"

    response = "Looks like I found these objects: " + ", ".join(detected_objects)
    
    if "bed" in detected_objects:
        response += ". It's time to relax!"
    elif "bottle" in detected_objects:
        response += ". Stay hydrated!"
    elif "laptop" in detected_objects:
        response += ". You seem to be working."
    return response
