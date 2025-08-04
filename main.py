from fastapi import FastAPI, HTTPException
from youtube_transcript_api import YouTubeTranscriptApi

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


