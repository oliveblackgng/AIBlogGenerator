from fastapi import FastAPI
from pydantic import BaseModel
from youtube_utils import get_transcript
from ai_generator import generate_blog

app = FastAPI()

class VideoRequest(BaseModel):
    url: str

@app.post("/generate-blog")
def generate(video: VideoRequest):
    
    transcript = get_transcript(video.url)
    
    blog = generate_blog(transcript)
    
    return {"blog": blog}