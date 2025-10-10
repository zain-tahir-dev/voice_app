import utils.transport
import utils.session
from flask import Flask, render_template, jsonify
import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
from deep_translator import GoogleTranslator

app = Flask(__name__)

def record_audio(filename="voice.wav", duration=5, fs=44100):
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, device=1)

    sd.wait()
    sf.write(filename, audio, fs)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/record")
def record():
    record_audio()
    recognizer = sr.Recognizer()
    with sr.AudioFile("voice.wav") as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        translated_text = GoogleTranslator(source='auto', target='ur').translate(text)
        return jsonify({"text": text, "translation": translated_text})
    except:
        return jsonify({"text": "Could not recognize speech", "translation": ""})

if __name__ == "__main__":
    app.run(debug=True)

