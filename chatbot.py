def simple_chatbot(detected_objects):
    if not detected_objects:
        return "I did not see any thing"
    elif 'bed' in detected_objects:
        return "it a bed here."
    elif 'tv' in detected_objects:
        return "it a TV here."
    else:
        return f"I noticed {', '.join(detected_objects)}. Cool Stuff!"
    
    # response = {
    #     "bed": "It looks like you are near a ved. want me to play sleep music",
    #     "tv": "TV is here. Do you want to see trending shows",
    #     "laptop": "Oh it looks laptop do you want any help with laptop",


    # }


print("\n  Chatbot")

for obj in objects:
    for obj in responses:
        print("🤖",responses[obj])