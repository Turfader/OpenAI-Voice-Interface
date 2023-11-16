import speech_recognition as sr
import pyaudio
import wave


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

    # Transcribe the saved audio file using PocketSphinx
    recognizer = sr.Recognizer()

    try:
        # Use the PocketSphinx recognizer to transcribe the audio file
        with sr.AudioFile("microphone_input.wav") as source:
            audio_data = recognizer.record(source)  # Read the entire audio file
            recognized_text = recognizer.recognize_sphinx(audio_data)
            return recognized_text
    except sr.UnknownValueError:
        return "Sphinx could not understand audio"
    except sr.RequestError as e:
        return f"Error with Sphinx recognition: {e}"


if __name__ == "__main__":
    # Usage:
    recorded_text = transcribe_microphone()
    print("Recorded Text:", recorded_text)
