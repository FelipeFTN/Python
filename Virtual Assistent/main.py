import speech_recognition as sr
import pyttsx3
import pywhatkit

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.say('Sistema Ligado')
engine.runAndWait()

def talk(textotalk):
	engine.say(textotalk)
	engine.runAndWait()

try:
	with sr.Microphone() as source:
		listener.adjust_for_ambient_noise(source)
		print('Say something!')
		audio = listener.listen(source)
		command = listener.recognize_google(audio, language='pt-br')
		command = command.lower()
		if 'bom dia' in command:
			talk('Bom Dia Felipe')
		print(command)
except:
	print("Say it again please!")