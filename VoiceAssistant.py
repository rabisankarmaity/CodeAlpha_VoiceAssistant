# Import necessary libraries
import speech_recognition as sr  # Library for speech recognition
import pyttsx3  # Library for text-to-speech conversion
import datetime  # Library for handling date and time
import random
import pyjokes  # Library for generating jokes
import requests  # Library for making HTTP requests

# Initialize the recognizer for speech recognition
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the voice to a female voice (change the index as needed)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to get a motivational quote
def get_motivational_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random")
        data = response.json()
        quote = data[0]['q']
        return quote
    except Exception as e:
        return f"Sorry, I couldn't fetch a motivational quote at the moment. {e}"

# Initial greeting and available commands
speak("Hello Rabi, I am Xavier. I can help you with the time, date, tell a joke, or share a motivational quote. What can I do for you now?")

while True:
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    text = r.recognize_google(audio).lower()
    print("You said:", text)

    if "exit" in text:
        speak("Goodbye! Have a great day.")
        break
    if "time" in text:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        response = f"The current time is {current_time}."
    elif "date" in text:
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        response = f"Today is {current_date}."
    elif "joke" in text:
        joke = pyjokes.get_joke()
        response = joke
    elif "motivation" in text:
        quote = get_motivational_quote()
        response = quote
    else:
        response = "oho...I am not able to do that."

    speak(response)

    if not "exit" in text:
        speak("What can I do for you now?")
