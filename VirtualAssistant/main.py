import speech_recognition as sr
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()


# Define a function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Initialize the speech recognizer
r = sr.Recognizer()


# Define a function to listen to microphone input
def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
            # Try to recognize the speech using Google Speech Recognition
            text = r.recognize_google(audio)
            print("You said: {}".format(text))
            return text
    except Exception:
        # If recognition fails, return an empty string
        print("Sorry, I couldn't understand what you said.")
        return ""


# Main loop
while True:
    # Listen for user input
    text = listen()
    if not text:
        continue
    # Respond to the user input
    if "hello" in text:
        speak("Hello, how can I help you today?")
    elif "goodbye" in text:
        speak("Goodbye, have a great day!")
        break
    else:
        speak("I'm sorry, I didn't understand what you said.")
