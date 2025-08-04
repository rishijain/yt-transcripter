# 🎬 yt-transcripter

A FastAPI backend that fetches YouTube video transcripts, with support for multiple languages.
---

## 🚀 Features

- Fetch YouTube video transcripts using `youtube-transcript-api`


---

## 🛠️ Requirements

- Python 3.7 or newer
- pip (Python package manager)

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourname/yt-transcripter.git
cd yt-transcripter
```

## 🐍 Create the virtual environment using Python 3

### 2. Create and activate the environment
```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
Using the requirements file:
```
pip install -r requirements.txt
```

Or install manually:
```
pip install fastapi uvicorn youtube-transcript-api
```

## ▶️ Running the Server
Start the FastAPI development server with:

```
uvicorn main:app --reload
```

This starts the app at:
```
http://127.0.0.1:8000
```

You can explore and test the API via Swagger UI:
```
http://127.0.0.1:8000/docs
```
