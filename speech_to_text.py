import speech_recognition as sr
import pyaudio
import wave
import keyboard


def transcribe_microphone():
    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Set audio parameters
    format = pyaudio.paInt16
    channels = 1
    rate = 16000
    chunk = 1024

    frames = []

    print("Press and hold the space bar to record...")

    # Record audio while the space bar is being held down
    keyboard.wait('space')
    print("Recording...")

    # Open microphone stream
    stream = audio.open(format=format, channels=channels,
                        rate=rate, input=True,
                        frames_per_buffer=chunk)

    while keyboard.is_pressed('space'):  # Continuously record while space is pressed
        data = stream.read(chunk)
        frames.append(data)

    print("Recording finished.")

    # Stop and close the microphone stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded audio as a WAV file
    wf = wave.open("input.wav", "wb")
    wf.setnchannels(channels)
    wf.setsampwidth(audio.get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(b"".join(frames))
    wf.close()

    # Transcribe the saved audio file using PocketSphinx
    recognizer = sr.Recognizer()

    try:
        # Use the PocketSphinx recognizer to transcribe the audio file
        with sr.AudioFile("input.wav") as source:
            audio_data = recognizer.record(source)  # Read the entire audio file
            recognized_text = recognizer.recognize_sphinx(audio_data)
            print(f'Sphinx thinks you said: {recognized_text}')
            return recognized_text
    except sr.UnknownValueError:
        return "Sphinx could not understand audio"
    except sr.RequestError as e:
        return f"Error with Sphinx recognition: {e}"


if __name__ == "__main__":
    # Usage:
    recorded_text = transcribe_microphone()
    print("Recorded Text:", recorded_text)
