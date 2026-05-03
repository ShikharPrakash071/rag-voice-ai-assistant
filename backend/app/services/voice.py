from faster_whisper import WhisperModel
from gtts import gTTS
import uuid
import os

# Audio folder
AUDIO_DIR = "backend/audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

# Load model once (important for performance)
model = WhisperModel(
    "base",
    compute_type="int8"  # CPU optimized (fast + low memory)
)

# Speech → Text
def speech_to_text(audio_path):
    segments, _ = model.transcribe(audio_path)
    text = " ".join([segment.text for segment in segments])
    return text.strip()


# Text → Speech
def text_to_speech(text):
    filename = f"{uuid.uuid4()}.mp3"
    filepath = os.path.join(AUDIO_DIR, filename)

    tts = gTTS(text=text)
    tts.save(filepath)

    return filename