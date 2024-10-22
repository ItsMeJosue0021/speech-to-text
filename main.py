import os
import sys
import wave
import json
import vosk
import pyaudio

def initialize_audio_stream():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000

    p = pyaudio.PyAudio()  # Initialize PyAudio
    stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK,
    )
    return stream

def main():
    if not os.path.exists("C:\\python\\vosk-model-small-en-us-0.15\\vosk-model-small-en-us-0.15"):
        print("Please download the model first.")
        sys.exit(1)

    model = vosk.Model("C:\\python\\vosk-model-small-en-us-0.15\\vosk-model-small-en-us-0.15")
    recognizer = vosk.KaldiRecognizer(model, 16000)

    # Initialize audio stream
    stream = initialize_audio_stream()

    while True:
        data = stream.read(4000)
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            print(result["text"])

    # Clean up
    stream.stop_stream()
    stream.close()
    # p.terminate()  # Terminate PyAudio

if __name__ == "__main__":
    main()
