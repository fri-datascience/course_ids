### Docker compose demo

This is a simple demo of how to use docker compose to run an app that uses multiple containers.

Our app uses 3 services:
- `streamlit-app`: A Streamlit app where we can upload an audio/video file and see the transcription.
- `whisper`: A server with a REST API that transcribes audio files.
- `redis`: A Redis server to store the transcriptions for faster access in the future.

### Setup:

#### A) Running each service individually:

**Whisper**
```
docker pull fedirz/faster-whisper-server:latest-cpu
docker run -p 8000:8000 --volume ~/.cache/huggingface:/root/.cache/huggingface --name whisper -d fedirz/faster-whisper-server:latest-cpu
```

You can test it from the gradio web interface or using curl:
`curl http://localhost:8000/v1/audio/transcriptions -F "file=@Recording.m4a" -F "language=en"`

**Redis**
```
docker pull redis
docker run -p 6379:6379 --name redis-transcript -d redis
```

**Streamlit app**

```bash
cd webapp
pip install -r requirements.txt
streamlit run app.py
```

#### B) using docker compose:

Run all services using `docker-compose up`