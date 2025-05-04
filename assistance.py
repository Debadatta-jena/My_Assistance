import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import pyjokes

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # speaking speed

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def greet_user():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your AI voice assistant. How can I help you?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User:", query)
    except sr.UnknownValueError:
        speak("Sorry, I did not catch that. Please say it again.")
        return "None"
    return query.lower()

def run_assistant():
    greet_user()
    while True:
        query = take_command()

        if 'time' in query:
            time_str = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {time_str}")

        elif 'date' in query:
            date_str = datetime.datetime.now().strftime("%A, %B %d, %Y")
            speak(f"Today is {date_str}")

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            try:
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia...")
                speak(result)
            except:
                speak("Sorry, I couldn't find anything on Wikipedia.")

        elif 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'how are you' in query:
            speak("I'm doing great. Thanks for asking!")

        elif 'your name' in query:
            speak("I am your AI assistant, created during your internship.")

        elif 'exit' in query or 'quit' in query:
            speak("Goodbye! Have a nice day.")
            break

        else:
            speak("I didn't understand that. Please try something else.")

if __name__ == "__main__":
    run_assistant()

