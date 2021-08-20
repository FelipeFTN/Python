import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime

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
	print(command)
	return command

def run():
	try:
		command = listen()
		if 'tocar' in command:
			print(command)
			song = command.replace('tocar', '')
			talk('Reproduzindo ' + song)
			pywhatkit.playonyt(song)
		elif 'pesquisar' in command:
			search = command.replace('pesquisar', '')
			information = wikipedia.summary(search, 1)
			talk(information)
		elif 'horário' in command:
			time = str(datetime.datetime.now().time())
			formatedTime = time.split(":")
			formatedTime.pop()
			time = str(formatedTime[0] + " e " + formatedTime[1])
			talk("Agora são " + time)
			print(time)
	except:
		run()

while True:
	run()
