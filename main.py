from gtts import gTTS

given_text = 'Hello, this is the test text'
tts = gTTS(given_text, lang='en', slow=False)

tts.save('tts.mp3')