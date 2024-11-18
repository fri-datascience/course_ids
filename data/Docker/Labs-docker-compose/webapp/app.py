import streamlit as st
import requests
import redis
import hashlib
import os

REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
WHISPER_HOST = os.getenv('WHISPER_HOST', 'localhost')

# Connect to Redis
redis_client = redis.StrictRedis(host=REDIS_HOST, port=6379, decode_responses=True)

def hash_audio(audio_bytes):
    """Generate a unique hash for the audio file."""
    return hashlib.md5(audio_bytes).hexdigest()

def transcribe_audio(audio_bytes):
    """Send audio to the faster-whisper-server for transcription."""
    whisper_url = f"http://{WHISPER_HOST}:8000/v1/audio/transcriptions"
    try:
        response = requests.post(
            whisper_url,
            files={"file": ("audio.wav", audio_bytes)},
            data={"language": "en"}
        )
        response.raise_for_status()
        return response.json().get("text", "")
    except requests.exceptions.RequestException as e:
        return None
    
def get_transcription(audio_hash, audio_bytes):
    """Retrieve the transcription from Redis or transcribe the audio using Whisper."""
    # Check
    cached_transcription = redis_client.get(audio_hash)
    if cached_transcription:
        return cached_transcription
    else:
        return transcribe_audio(audio_bytes)

st.title("Audio Transcription 🎙️")
uploaded_file = st.file_uploader("Upload an audio/video file", type=["wav", "mp3", "m4a", "mp4", "mkv"])

if uploaded_file is not None:
    if st.button("Transcribe", type="primary"):
        audio_bytes = uploaded_file.read()
        audio_hash = hash_audio(audio_bytes)

        with st.spinner("Transcribing audio..."):
            transcription = get_transcription(audio_hash, audio_bytes)

        if transcription:
            st.header("Transcription:")
            st.write(transcription)
            
            # Save the transcription
            redis_client.set(audio_hash, transcription)


st.divider()

if st.button("Clear Cache 🗑️"):
    redis_client.flushall()

num_cache_items = len(redis_client.keys())
st.write(f"Number of items in cache: {num_cache_items}")