from faster_whisper import WhisperModel
from gtts import gTTS
import os
import time

# 🔥 Audio folder setup
AUDIO_DIR = "audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

# 🔥 Load Whisper model once (performance)
model = WhisperModel("base")


# 🎤 Speech → Text
def speech_to_text(audio_path):
    segments, _ = model.transcribe(audio_path)
    text = " ".join([seg.text for seg in segments])
    return text


# 🔊 Text → Speech (saved in audio folder with unique name)
def text_to_speech(text):
    filename = f"response_{int(time.time())}.mp3"
    output_path = os.path.join(AUDIO_DIR, filename)

    tts = gTTS(text)
    tts.save(output_path)

    return output_path