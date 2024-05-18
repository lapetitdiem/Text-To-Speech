from gtts import gTTS
from langdetect import detect
import os
import pygame

def textToSpeech(given_text) : 
    detect_language = detect(given_text)
    tts = gTTS(given_text, lang=detect_language, slow=False)
    current_directory = os.path.dirname(__file__)
    parent_directory = os.path.dirname(current_directory)
    
    target_folder = os.path.join(parent_directory, 'MP3')
    speech_file = os.path.join(target_folder, 'tts.mp3')

    # # # Specify the file path

    # # Save the speech file
    tts.save(speech_file)
    # pygame.init()
    # pygame.mixer.music.load(speech_file)
    # pygame.mixer.music.play()

    # while pygame.mixer.music.get_busy():
    #     pygame.time.Clock().tick(10)

    # pygame.quit()
    return 'tts.mp3'
