
from re import search
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate',158)

import speech_recognition as sr
import datetime
import warnings
import calendar
import random
import wikipedia
from gtts import gTTS




#ignore any warning messages
warnings.filterwarnings('ignore')

# Record audio and return it as a string
def recordAudio():

    # record the audio
    r = sr.Recognizer() # Creating a recognizer obj

    #open the mic and start recording
    with sr.Microphone() as source:
        print('Say something: ')
        audio = r.listen(source)
    
    # Use Googles Speech recognition
    data = ''
    try: 
        data = r.recognize_google(audio)
        print('User: ' + data )
    except sr.UnknownValueError: # Check for unknown error
        print('Google Speech Recognition could not understand the audio, unknown error')
    except sr.RequestError as e:
        print('Request results from Google Speech Recognition service error' + e)

    return data

# Function to get the assistant(Polo) response
def marcoResponse(text):
    print("Marco: " + text)
    
    engine.say(text)
    engine.runAndWait()
  
# Function for wake word or phrase
def wakeWord(text):
    WAKE_WORDS = ['Oh Marco', 'marco', 'avocado'] # a list of wake words

    text = text.lower()

    #check to see if users command/text contains a wake words/phrase
    # my favorite part
    for phrase in WAKE_WORDS:
        if phrase in text:
            print('Marco: Polo')
            engine.say('Polo!')
            engine.runAndWait()
    return ' '
            
    

# function to give current date

def getDate():
    x = datetime.datetime.now()
    day = x.strftime("%dth")# day number
    weekday = x.strftime("%A") #dayname
    month = x.strftime("%B")
    year = x.strftime("%Y")
    

    date = 'Today is ' + weekday + ' ' + month + ' ' + day + ' ' + year
    
    return date 


def Question(text):
    CONV = ['how are you', 'how are you doing', 'whats up' ]
    ANS = ['I am good', 'Not bad', 'I am fine ', 'I have seen better days']
    if text.lower() in CONV:
        reply = random.choice(ANS)
        print('Marco: ' + reply)
        engine.say(reply)
        engine.runAndWait()
    else:
        return True
        
# function to greet
def Greeting(text):
    GREETING_INPUTS = ['hi', 'hello', 'hey', 'hola' ]

    GREETING_RESPONSE = [' Howdy', 'hey', 'sup dude', 'bonjour']

    # if the users input us a greeting_input, return greeting_response randomly
    words = text.split()
    for word in words:
        if word.lower() in GREETING_INPUTS:
            engine.say(random.choice(GREETING_RESPONSE))
            engine.runAndWait()
        else:
            return True
        
 

#function to get firstname and lastname from the text
def Search(text):
    try:
        text = text.split()
        text.remove('search')
        text = ''.join(text)
        information = wikipedia.summary(text, sentences= 1)
        print('Marco: ' + information)
        engine.say(information)
        engine.runAndWait()
    except:
        print('Please be more specific')


#function to gettime
def getTime():
    time = datetime.datetime.now()
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    meridiem = time.strftime("%p")
    time = 'it is ' + hour + '.' + minute + ' ' + meridiem
    return time
    
def Sleep():
   
    print('Marco: Goodbye!')
    engine.say("Goodbye!")
    engine.runAndWait()
   
   
#==================================================================================
    #==================RUNNING =====================================#
#===================================================================================

print("Marco: Hello, my name is Marco. I'll be your Assistance.")

print(' date in text = get the date')
print(' time in text  = get time')
print(' search in text =  search the thing you ask in wikipedia')
print('          ')
print(' ')
engine.say("Hello, my name is Marco. I'll be your Assistance")
engine.runAndWait()
WAKE_WORDS = ['Oh Marco', 'marco', 'avocado']

while True:
    text = recordAudio()
    Greeting(text)  
    wakeWord(text)
    Question(text)
    
    if 'date' in text:
        response = getDate()
        marcoResponse(response)
    elif 'time' in text:
        response = getTime()
        marcoResponse(response)
    elif text.startswith('search') == True:
        Search(text)
    elif 'sleep' in text:
        Sleep()
        break



        









'''
 #record the audio
    text = recordAudio()
    Greeting(text)  
    wakeWord(text)
    Question(text)
    
    if 'date' in text:
        getDate()

            #search
    elif text.startswith('search') == True:
        Search(text)
        
        #gettime
    elif 'time' in text:
        getTime()
    
    elif 'sleep' in text:
        print('Marco: Goodbye!')
        engine.say("Goodbye!")
        engine.runAndWait()
        break
    
'''





