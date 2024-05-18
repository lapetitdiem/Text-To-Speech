from flask import Flask, render_template, request,send_from_directory
from Text_To_Speech.convert import textToSpeech
import os
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('givenText.html')

@app.route('/convertToSpeech', methods=['POST'])
def result() :
    textInput = request.form['textInput']
    mp3_path = textToSpeech(textInput)
    return render_template('inputResult.html', data =textInput, mp3_filename=mp3_path)

@app.route('/MP3/<filename>')
def serve_mp3(filename):
    print(os.path.join(app.root_path,'MP3',filename))
    return send_from_directory(os.path.join(app.root_path,'MP3'),filename)

if __name__ == "__main__":
    app.run(debug=True)