import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Set to a female voice

# Set to a soft-toned female voice (you may need to experiment with different indices)
engine.setProperty('voice', voices[1].id)

# Adjust voice properties for a softer tone
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 0.7)  # Volume (0.0 to 1.0)

# Initialize speech recognition
r = sr.Recognizer()

def speak(text, member="Queeny"):
    print(f"{member}: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(f"User: {text}")
            return text
        except:
            print("Sorry, I didn't catch that.")
            return ""