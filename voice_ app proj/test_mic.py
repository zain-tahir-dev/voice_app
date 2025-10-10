import sounddevice as sd
import soundfile as sf

fs = 44100  # sample rate
seconds = 5  # record for 5 seconds

print("🎤 Recording... Speak now!")
audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()
sf.write("test.wav", audio, fs)
print("✅ Saved as test.wav. Play it to check your voice.")
