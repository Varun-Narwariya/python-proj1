import webbrowser as wb
import speech_recognition as sr
import pyttsx3 as p3
 #install py audio


engine=p3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()
with sr.Microphone() as source:
    print("listning")
    audio=r.listen(source)
try:
    cmd=r.recognize_google(audio)
    print(cmd)
except sr.UnknownValueError:
    print("error")

result = cmd.split()


str="https://www.youtube.com"
str=str.replace("youtube",result[1])
wb.open(str)