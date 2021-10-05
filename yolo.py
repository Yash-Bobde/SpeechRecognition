#command to be given like alexa play the song name lol.
#or command like who is ratan tata
# or go like where is paris
# ask what's the time right now
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            talk('My ears are awaiting for your beautiful voice...')
            print('My ears are awaiting for your beautiful voice...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)

    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing the song which you like only for you Ash' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M:%S')
        print(time)
        talk('CURRENT TIME ROUND YOU IS '+ time)
    elif 'who is' in command:
        person = command.replace('who is ', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'where is' in command:
        place = command.replace('where is ', '')
        dest = wikipedia.summary(place, 2)
        print(dest)
        talk(dest)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk("can you please repeat it for me.")

while True:
    run_alexa()
