from gtts import gTTS
from tempfile import NamedTemporaryFile

def speak(text):
    tts = gTTS(text)
    f = NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(f.name)
    return f.name