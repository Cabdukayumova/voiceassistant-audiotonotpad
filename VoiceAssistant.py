import time
import playsound
import datetime
import pyttsx3
import speech_recognition as sr
from gtts import gTTS
import pytz
import subprocess

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)
		said = ""

		try:
			said = r.recognize_google(audio)
			print(said)
		except Exception as e:
			print("Exception" + str(e))

	return said
'''
text = get_audio()

if "hello" in text:
	speak("hello, how are you?")'''

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])

text = get_audio().lower()

NOTE_STRS = ["make a note", "write this down", "remember this", "type this"]
for phrase in NOTE_STRS:
    if phrase in text:
        speak("What would you like me to write down? ")
        write_down = get_audio()
        note(write_down)
        speak("I've made a note of that.")