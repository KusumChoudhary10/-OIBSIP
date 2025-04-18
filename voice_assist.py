import os
import time
import speech_recognition as sr
from gtts import gTTS
import pyglet
import random

pyglet.options['audio'] = ('openal', 'directsound', 'pulse')

def speak(text):
    try:
        tts = gTTS(text=text, lang='en')
        filename = "voice.mp3"
        tts.save(filename)

        music = pyglet.media.load(filename, streaming=False)
        player = pyglet.media.Player()
        player.queue(music)
        player.play()

        # Close the app when the audio finishes
        def close_app(dt):
            pyglet.app.exit()

        pyglet.clock.schedule_once(close_app, music.duration)
        pyglet.app.run()

        os.remove(filename)
    except Exception as e:
        print("Speak Error:", str(e))

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        try:
            audio  = r.listen(source, timeout=5, phrase_time_limit=7)
            said = r.recognize_google(audio)
            print("You said:", said)
            return said
        except sr.WaitTimeoutError:
            print("You didn’t say anything.")
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand.")
        except sr.RequestError:
            print("Network issue or Google API down.")
        except Exception as e:
            print("Other error:", str(e))
    return ""

jokes = ["Parallel lines have so much in common. It’s a shame they’ll never meet.",
         "Why do programmers prefer dark mode? Because light attracts bugs"]

greetings = ["Hi there!", "Hello!", "Hey! What's up?", "How can I help you today?"]
speak(random.choice(greetings))



while True:   # no empty commands allowed 
    command = get_audio()
    if command:
        command = command.lower()
        if "bye" in command or "stop" in command:
            speak("okay  bye. Run the code again to talk to me!")
            break
        elif "hello" in command:
            speak("Hello! How can I help you ?")
        elif "your name" in command:
            speak(" My name is Miyo")
        elif "joke" in command:
            joke = random.choice(jokes)
            speak(joke)
        elif "mum" in command:
            speak("hello mother, how are you")
        elif "fine" in command:
            speak("that is good")
        elif "my name" in command:
            speak("Your name is kusum choudhary")
        
        else:
            speak("I did not understand that. Please try again.")
    else:
        print("No command detected. Please try speaking again.")
