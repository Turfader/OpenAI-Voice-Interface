import io
import pyaudio
import wave
from google.cloud import speech
from google.cloud import speech_v1p1beta1 as speech
from google.cloud.speech_v1p1beta1 import enums


def transcribe_microphone():
    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Set audio parameters
    format = pyaudio.paInt16
    channels = 1
    rate = 16000
    chunk = 1024
    record_seconds = 5  # Adjust as needed

    # Open microphone stream
    stream = audio.open(format=format, channels=channels,
                        rate=rate, input=True,
                        frames_per_buffer=chunk)
    print("Recording...")

    frames = []

    # Record audio from the microphone
    for i in range(0, int(rate / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)

    print("Recording finished.")

    # Stop and close the microphone stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded audio as a WAV file
    wf = wave.open("microphone_input.wav", "wb")
    wf.setnchannels(channels)
    wf.setsampwidth(audio.get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(b"".join(frames))
    wf.close()

    # Transcribe the saved audio file using Google Cloud Speech-to-Text API
    client = speech.SpeechClient()

    with io.open("microphone_input.wav", "rb") as audio_file:
        content = audio_file.read()

    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=rate,
        language_code="en-US"
    )

    response = client.recognize(config=config, audio=audio)

    # Extract transcribed text
    transcribed_text = ""
    for result in response.results:
        transcribed_text += result.alternatives[0].transcript + " "

    return transcribed_text

# Transcribe speech from microphone
recorded_text = transcribe_microphone()
print("Recorded Text:", recorded_text)
