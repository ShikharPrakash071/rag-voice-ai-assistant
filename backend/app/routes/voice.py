import os
import shutil

from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse

from app.services.voice import speech_to_text, text_to_speech
from app.routes.query import query

router = APIRouter()

@router.post("/voice-query")
async def voice_query(file: UploadFile = File(...)):
    
    # Save audio
    audio_path = "temp_audio.wav"
    with open(audio_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    #  Speech → text
    question = speech_to_text(audio_path)

    #  Text → RAG answer
    result = query(question)
    answer = result["answer"]

    #  Text → speech
    output_audio = text_to_speech(answer)

    #  Return audio directly (auto play)
    return FileResponse(
        path=output_audio,
        media_type="audio/mpeg"
    )

# FOR UNDERSTANDING THE FLOW ONLY.
# Audio upload 
# → speech_to_text
# → RAG
# → text_to_speech
# → FileResponse 

# NOW THIS IS THE FLOW:
#  Browser will open audio
#  or it will download the responsed audio
#  CONS:-
# JSON formated response is not possiblefrom now on. 
# It will only return audio file. So, if we want to send any other data,
# we need to embed it in the audio file name or use some other method. 