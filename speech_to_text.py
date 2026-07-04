import speech_recognition as sr
from pydub import AudioSegment
import tempfile
import os

def speech_to_text(uploaded_file):
    recognizer = sr.Recognizer()

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
        temp_file.write(uploaded_file.read())
        temp_path = temp_file.name

    audio = AudioSegment.from_file(temp_path)
    audio.export(temp_path, format="wav")

    with sr.AudioFile(temp_path) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data)
    except Exception:
        text = "Speech could not be recognized."

    os.remove(temp_path)

    return text