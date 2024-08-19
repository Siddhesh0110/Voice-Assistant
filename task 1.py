import speech_recognition as sr
import pyttsx3
import wikipedia

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            command = None
        except sr.RequestError:
            speak("Sorry, the service is down.")
            command = None

    return command

def main():
    speak("Hello! How can I help you today?")
    
    while True:
        command = listen()

        if command:
            if 'wikipedia' in command:
                speak("Searching Wikipedia...")
                command = command.replace("wikipedia", "")
                results = wikipedia.summary(command, sentences=2)
                speak("According to Wikipedia")
                speak(results)

            elif 'exit' in command or 'bye' in command:
                speak("Goodbye!")
                break

            else:
                speak("Sorry, I can only search Wikipedia or exit. Try saying something like 'search Wikipedia for Python programming'.")
        
if __name__ == "__main__":
    main()
