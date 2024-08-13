import speech_recognition as sr
import pyttsx3
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
tts_engine = pyttsx3.init()

# Set up OpenAI API using environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

# List all available voices and choose a female voice
# voices = tts_engine.getProperty('voices')
# female_voice_id = None
# for voice in voices:
#     if 'female' in voice.name.lower():  # You might need to adjust this based on your system
#         female_voice_id = voice.id
#         break

# if female_voice_id:
#     tts_engine.setProperty('voice', female_voice_id)
# else:
#     print("Female voice not found. Using default voice.")

def ask_openai(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can use "gpt-4" if available in your API plan
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ]
        )
        return response.choices[0].message["content"]
    except openai.error.RateLimitError:
        return 'Rate limit exceeded. Please wait and try again.'
    except openai.error.OpenAIError as e:
        print(f"An error occurred: {e}")
        return None

def recognize_speech_from_mic():
    # Get the default microphone
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio)
            print(f"You: {text}")

            # Check for the exit command
            if text.lower() == "exit":
                print("Assistant: Goodbye, Take care!")
                tts_engine.say("Goodbye, Take care!")
                tts_engine.runAndWait()
                print("Exiting...")
                return False  # Return False to indicate the loop should stop

            # Get a response from OpenAI
            response = ask_openai(text)
            print(f"Assistant: {response}")

            # Speak the response
            if response:
                tts_engine.say(response)
                tts_engine.runAndWait()

        except sr.UnknownValueError:
            unknownSpeechMessage = "Sorry, I could not understand the audio.";
            print(f'Assistant: {unknownSpeechMessage}')
            tts_engine.say(unknownSpeechMessage)
            tts_engine.runAndWait()

        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")
            tts_engine.say("Assistant: Sorry, there was an error with the speech recognition service.")
            tts_engine.runAndWait()

    return True

if __name__ == "__main__":
    while recognize_speech_from_mic():
        pass  
