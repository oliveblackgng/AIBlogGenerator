from youtube_transcript_api import YouTubeTranscriptApi
import re

def get_video_id(url):
    pattern = r"v=([a-zA-Z0-9_-]+)"
    match = re.search(pattern, url)
    return match.group(1)

def get_transcript(url):
    
    video_id = get_video_id(url)

    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    text = " ".join([t['text'] for t in transcript])

    return text