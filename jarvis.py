from pywhatkit.mainfunctions import search
import speech_recognition as sr
import pyttsx3
import pywhatkit

name = "jarvis"
listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice)
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, "")
                print(rec)
        
    except:
        pass
    return rec

def run():
    rec = listen()
    if "reproduce" in rec:
        music = rec.replace("reproduce", "reproduceme", "cargame", "carga" "")
        talk("Reproduciendo" + music)
        pywhatkit.playonyt(music)

    if "busca" in rec:
        search = rec.replaace("busca" "")
        talk("Buscando" + search)
        pywhatkit.playonyt(search)

run()

