import speech_recognition as sr
listener = sr.Recognizer()
try:
	with sr.Microphone() as source:
		listener.adjust_for_ambient_noise(source)
		print('Say something!')
		audio = listener.listen(source)
		command = listener.recognize_google(audio)
		print(command)
except:
	pass