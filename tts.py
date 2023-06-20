from flask import Flask, render_template, request, send_file
from gtts import gTTS
import os


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    text=request.form['text']
    tts=gTTS(text=text, lang="en")
    filename="generated.mp3"
    tts.save(filename)
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.debug = True
    app.run()

