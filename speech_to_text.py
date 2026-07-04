import whisper

# Load Whisper model once
model = whisper.load_model("base")

def transcribe_audio(file_path):
    """
    Convert speech to text using Whisper.
    """
    result = model.transcribe(file_path)
    return result["text"]