from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import upload, query, voice
app = FastAPI()
app.include_router(upload.router)
app.include_router(query.router)
app.include_router(voice.router)
app.mount("/audio", StaticFiles(directory="audio"), name="audio")

@app.get("/")
def home():
    return {"message": "API is working"}