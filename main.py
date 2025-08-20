from fastapi import FastAPI, HTTPException
from youtube_transcript_api import YouTubeTranscriptApi
from pytubefix import YouTube
from pytubefix.cli import on_progress
import uuid
import datetime


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/videos/languages/{video_id}")
def get_video_languages(video_id: str):
    try:
          ytt_api = YouTubeTranscriptApi()
          transcript_list = ytt_api.list(video_id)
       
          languages = [
              {
                  "language_code": transcript.language_code,
                  "language": transcript.language,
                  "is_generated": transcript.is_generated
              }
              for transcript in transcript_list
          ]

          return {"video_id": video_id, "available_languages": languages}

    except Exception as e:
          raise HTTPException(status_code=500, detail=str(e))
    

@app.get("/videos/transcript/{video_id}/{language_code}")
def get_video_transcript(video_id: str, language_code: str):
    try:
        transcript = YouTubeTranscriptApi().fetch(video_id, languages=[language_code])

        return {"video_id": video_id, "language_code": language_code, "transcript": transcript}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/videos/download-audio/{video_id}")
def download_video(video_id: str):
    try:
        # Logic to download the video
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        yt = YouTube(video_url, on_progress_callback=on_progress)
        ys = yt.streams.get_audio_only()

        # Generate unique filename
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        unique_id = str(uuid.uuid4())[:8]
        filename = f"audio_{video_id}_{timestamp}_{unique_id}.m4a"

        ys.download(output_path="/Users/rishi/Downloads", filename=filename)
        full_path = f"/Users/rishi/Downloads/{filename}"
        return {"path": full_path, "status": "downloaded", "filename": filename}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
