import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()

engine = pyttsx3.init()


try:
    with sr.Microphone() as source:
        print("Escuchando...")
        voice = listener.listen(source)
        rec = listener.recognize_google(voice)
        print(rec)
        
except:
    pass


voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

engine.say("Buenas noches Rafael")
engine.runAndWait()



