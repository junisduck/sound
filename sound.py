import wave
import pyaudio
import uvicorn
from fastapi import FastAPI, Response, Request
import requests

chunk = 1024
path = '/Users/user/Downloads/ding.wav'

app = FastAPI()

@app.get("/")
def sound():
    with wave.open(path, 'rb') as f:
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                        channels=f.getnchannels(),
                        rate=f.getframerate(),
                        output=True)
        data = f.readframes(chunk)
        while data:
            stream.write(data)
            data=f.readframes(chunk)
        stream.close()
        p.terminate()

if __name__ == "__main__":
    uvicorn.run("sound:app", host="0.0.0.0", port=8888, log_level="debug", reload=True)