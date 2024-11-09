# Python program to translate speech to text and text to speech
import speech_recognition as sr
import pyttsx3
import os
from dotenv import load_dotenv
import openai

# Load environment variables
load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_KEY")  # Corrected the typo in the key name

# Set up OpenAI API key
openai.api_key = OPENAI_KEY

# Function to convert text to speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# Initialize the recognizer
r = sr.Recognizer()  # Corrected initialization method

def record_text():
    # Loop in case of error
    while True:
        try:
            # Use the microphone as source for input
            with sr.Microphone() as source2:
                # Prepare recognizer to receive input
                r.adjust_for_ambient_noise(source2, duration=0.2)
                print("I'm listening")

                # Listen for the user's input
                audio2 = r.listen(source2)

                # Use Google to recognize the audio
                Mytext = r.recognize_google(audio2)
                return Mytext

        except sr.RequestError as e:
            print(f"Could not request results; {e}")

        except sr.UnknownValueError:
            print("Unknown error occurred")

def send_to_chatGpt(messages, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].message.content
    messages.append({"role": "assistant", "content": message})  # Add assistant's response to messages
    return message

messages = [{"role": "user", "content": "Please act like Jarvis from Iron Man"}]
while True:
    # Get user speech as text
    text = record_text()
    messages.append({"role": "user", "content": text})

    # Send conversation to ChatGPT
    response = send_to_chatGpt(messages)
    
    # Speak the response
    SpeakText(response)
    print(response)
