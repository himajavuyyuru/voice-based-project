import librosa
import numpy as np

def load_audio(file_path):
    """
    Load an audio file.
    """
    audio, sr = librosa.load(file_path, sr=None)
    return audio, sr


def extract_features(audio, sr):
    """
    Extract basic audio features.
    """
    features = {
        "duration": librosa.get_duration(y=audio, sr=sr),
        "mean_amplitude": float(np.mean(np.abs(audio)))
    }
    return features