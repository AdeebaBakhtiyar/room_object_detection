 Room AI – YOLO-Based Object Detection with Chatbot & Voice Feedback
An interactive AI project that detects room objects using YOLO, responds with chatbot messages, and speaks results aloud — all in one smart interface.

🚀 Project Objective
This project was developed to detect objects in the room using yolo version 8 which supports the voice assistant and chatbot.

Features
Real-time image capture from your webcam

YOLOv8 object detection on room images

Chatbot response based on detected objects

Voice output using Google Text-to-Speech (gTTS)

Interactive Streamlit web app 


Tech Stack
YOLOv8 – For real-time object detection

Streamlit – To build the web interface

OpenCV & PIL – Image handling

gTTS – Voice synthesis for detected objects

Python 3.10+

📂 Folder Structure
room_object_detection
├── app.py             # Main Streamlit app
├── detect.py          # YOLOv8 detection logic
├── chatbot.py         # Rule-based chatbot logic
├── speak.py           # Voice synthesis with gTTS
├── requirements.txt   # All Python dependencies

How to Run Locally
# 1. Clone the repository
git clone https://github.com/your-username/room_object_detection.git
cd yolo-room-ai

# 2. Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install requirements
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
🌐 Free Online Deployment
Deploy your app to Streamlit Cloud for free:

Push this repo to GitHub

Go to Streamlit Cloud → New App

Select your GitHub repo and app.py as the entry point

Click Deploy

💡 Tip: Make sure to include your requirements.txt in the GitHub repo.