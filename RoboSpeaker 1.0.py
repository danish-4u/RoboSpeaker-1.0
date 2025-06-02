import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)  

print("Welcome to RoboSpeaker")
while True:
    x = input("Enter word to Speak: ")
    if x == 'q':
        break
    engine.say(x)
    engine.runAndWait()
