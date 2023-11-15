from gtts import gTTS
import pygame
# come back to the playsound library! It just doesn't want to work rn


def read(text):
    # Text to be converted to speech
    tts = gTTS(text=text, lang='en')  # Language selected here is English ('en')

    # Save the speech as an MP3 file
    output_file = "output.mp3"
    tts.save(output_file)

    # Initialize Pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load(output_file)
    pygame.mixer.music.play()

    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


if __name__ == "__main__":
    read("hello world")
