#import the necessary libraries
import streamlit as st
import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
import datetime
import pyjokes as pj
import pywhatkit
import time

# Function to speak text
def speak(text):
    engine = pyttsx3.init()
    id = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
    engine.setProperty('voice', value=id)
    engine.say(text=text)
    engine.runAndWait()

# Function for speech recognition
def speech_recog():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.sidebar.write('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source, 0, 8)
        try:
            st.sidebar.write('Recognizing...')
            query = r.recognize_google(audio, language='en')
            return query.lower()
        except sr.UnknownValueError:
            st.sidebar.write('Speech Recognition could not understand audio')
            return ''
        except sr.RequestError as e:
            st.sidebar.write(f'Speech Recognition request failed; {e}')
            return ''

# Function to handle main functionalities
def main(query):
    Query = str(query).lower()
    if 'hello' in Query:
        speak('Hello! How can I help you?')
    elif 'bye' in Query:
        speak('Goodbye! Have a nice day!')
    elif 'joke' in Query:
        joke =pj.get_joke(language='en',category='neutral')
        speak(joke)
    elif 'open youtube' in Query:
        speak('Opening YouTube')
        webbrowser.open('https://www.youtube.com')
        time.sleep(2)
    elif 'google' in Query:
        speak('Opening Google')
        webbrowser.open('https://www.google.com')

    elif 'chat gpt' in Query:
        speak('Opening ChatGPT')
        webbrowser.open('https://chat.openai.com')

    elif 'wikipedia' in Query:
        speak('Searching in  Wikipedia...')
        query = Query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=3)
        print('')
        speak(results)
    
    elif 'who' in Query:
        print('I am Jarvis an simple assistant Created by Naeem Bozdar:)')

    elif 'what' in Query:
        print('My name is Jarvis an simple assistant .')

    elif 'time' in Query:
        current_time=datetime.datetime.now().strftime('%H:%M')
        speak(f'The Current Time is {current_time}')
    elif 'creator' in Query:
        speak('My Creator is Naeem Bozdar')

    elif 'day' in Query:
        date = datetime.date.today()
        speak(f'Today is {date}')

    elif 'search in yt' in Query:
        speak('What do you want to search on YouTube?')
        search_query = speech_recog()
        pywhatkit.playonyt(search_query)
    elif 'find in'  in Query:
        speak('What do you want to search on Google?')
        search_query = speech_recog()
        pywhatkit.search(search_query)
    elif 'linkedin' in Query:
        speak('Opening LinkedIn')
        webbrowser.open('www.linkedin.com')
    elif 'remined' in Query:
        speak('Yeah,On monday 9PM you have a to attend lab in Univeristy')

    elif 'your creator' in Query:
       speak('Naeem Bozdar is my creator who is studying Computer System Engineering in Dawood University Of Engineering and Technology.He has some Expertiese in python.')
    

# Streamlit UI
def run_jarvis():
    st.sidebar.title('Jarvis Voice Assistant')
    st.sidebar.write('Press the button and speak your command.')
    
    if st.sidebar.button('Speak'):
        query = speech_recog()
        st.sidebar.write(f'You said: {query}')
        main(query)
    
    st.image('jarvis_logo.png', use_column_width=True)  # Add your Jarvis image here

if __name__ == '__main__':
    run_jarvis()
