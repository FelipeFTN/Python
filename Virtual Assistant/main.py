import speech_recognition as sr
import pyttsx3
import pywhatkit

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(textotalk):
	engine.say(textotalk)
	engine.runAndWait()

def listen():
	try:
		with sr.Microphone() as source:
			listener.adjust_for_ambient_noise(source)
			print('Escutando...')
			audio = listener.listen(source)
			command = listener.recognize_google(audio, language='pt-br')
			command = command.lower()
			if 'computador' in command:
				command = command.replace('computador', '')
	except:
		pass
	return command

def run():
	command = listen()
	if 'tocar' in command:
		song = command.replace('tocar', '')
		talk('Reproduzindo ' + song)
		pywhatkit.playonyt(song)

while True:
	run()