from gtts import gTTS
from playsound import playsound


def read(text):
    # Text to be converted to speech
    tts = gTTS(text=text, lang='en')  # Language selected here is English ('en')

    # Save the speech as an MP3 file
    output_file = "output.mp3"
    tts.save(output_file)

    playsound(output_file)


if __name__ == "__main__":
    read("hello world")
