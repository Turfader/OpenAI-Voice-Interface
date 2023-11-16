from gtts import gTTS
import os
import sys
# I have abandoned the playsound library. Pygame works. I'm not touching it.


def read(text):
    # Text to be converted to speech
    tts = gTTS(text=text, lang='en')  # Language selected here is English ('en')

    # Save the speech as an MP3 file
    output_file = "output.mp3"
    if os.path.exists(output_file):
        os.remove(output_file)
    tts.save(output_file)

    # Redirect stdout to a null device
    with open(os.devnull, 'w') as devnull:
        sys.stdout = devnull
        import pygame
        sys.stdout = sys.__stdout__  # Restore stdout

    # Initialize Pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load(output_file)
    pygame.mixer.music.play()

    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.quit()



if __name__ == "__main__":
    read("hello world")
