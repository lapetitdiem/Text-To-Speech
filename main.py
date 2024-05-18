from gtts import gTTS
from langdetect import detect
import os
import pygame

from flask import Flask, render_template, request


given_text = 'this is a test voice'
detect_language = detect(given_text)
tts = gTTS(given_text, lang=detect_language, slow=False)

current_directory = os.path.dirname(__file__)

parent_folder = os.path.join(current_directory, 'MP3')
# # Specify the file path
speech_file = os.path.join(parent_folder, 'tts.mp3')

# Save the speech file
tts.save(speech_file)
pygame.init()
pygame.mixer.music.load(speech_file)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

pygame.quit()