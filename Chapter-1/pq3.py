# pip install pyttsx3 to speech
import pyttsx3
engine = pyttsx3.init()
 
engine.say("Hello, This is Shahid!")
engine.runAndWait()