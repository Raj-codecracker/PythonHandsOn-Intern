import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Start Speaking...")
    r.adjust_for_ambient_noise(source)  # reduces noise
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print("You said:", text)

except sr.UnknownValueError:
    print("Sorry, I could not understand your speech.")

except sr.RequestError:
    print("Could not reach Google Speech API (check internet connection).")
