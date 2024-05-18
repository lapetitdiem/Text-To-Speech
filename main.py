from flask import Flask, render_template, request,send_from_directory, session
from To_Speech.convert import textToSpeech
from datetime import datetime
import os
app = Flask(__name__)
app.secret_key = '04468aff0e3acbb6c65b62e4150e227d'
@app.route('/')
def index():
    history = session.get('history',[])
    return render_template('givenText.html',history = history)

@app.route('/convertToSpeech', methods=['POST'])
def result() :
    textInput = request.form['textInput']
    mp3_path = textToSpeech(textInput)
    history = session.get('history',[])
    history.append(textInput)
    session['history'] = history
    return render_template('inputResult.html', data =textInput, mp3_filename=mp3_path)

@app.route('/MP3/<filename>')
def serve_mp3(filename):
    print(os.path.join(app.root_path,'MP3',filename))
    return send_from_directory(os.path.join(app.root_path,'MP3'),filename)

if __name__ == "__main__":
    app.run(debug=True)