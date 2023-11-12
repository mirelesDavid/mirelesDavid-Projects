from datetime import datetime
import speech_recognition as sr
import pyttsx3
import openai
import webbrowser
import pywhatkit as kit
import os


openai.api_key = "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"
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Busca la voz deseada por su nombre
desired_voice = "Microsoft Zira Desktop - English (United States)"
selected_voice = None

for voice in voices:
    if voice.name == desired_voice:
        selected_voice = voice
        break

if selected_voice is not None:
    # Establece la voz seleccionada
    engine.setProperty('voice', selected_voice.id)
else:
    print(f"La voz '{desired_voice}' no fue encontrada en las voces disponibles.")

# Puedes configurar la velocidad de habla aquí si lo deseas
engine.setProperty('rate', 30)
engine.setProperty('pitch', 10)


activationWord = 'charles'

def stop_speaking():
    engine.stop()


#SPEACH RECOGNITION
def parseCommand():
    listener = sr.Recognizer()
    print('Listening for a command')

    with sr.Microphone() as source:
        listener.pause_threshold = 2
        input_speech = listener.listen(source)

    try:
        print('Recognizing speech...')
        query = listener.recognize_google(input_speech, language='en-US') 
        print(f'The input speech was: {query}')

    except sr.UnknownValueError:
        print('I did not catch that. Please speak clearly.')
        return 'None'
    except sr.RequestError as e:
        print(f"Could not request results: {e}")
        return 'None'

    return query


#OPEN AI
def get_openai_response(query):
    model_engine = "gpt-3.5-turbo"
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": query}],
        max_tokens= 50,
        temperature=0.5
    )
    return response.choices[0].message["content"].strip()

#Get date
def get_current_datetime():
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    current_date = now.strftime("%Y-%m-%d")
    return f"The current time is {current_time} and the current date is {current_date}"


#GETS THE BEST WIKIPEDIA PAGE
def search_wikipedia(keyword=''):
    searchResults = wikipedia.search(keyword)
    if not searchResults:
        return 'No result received'
    try: 
        wikiPage = wikipedia.page(searchResults[0]) 
    except wikipedia.DisambiguationError as error:
        wikiPage = wikipedia.page(error.options[0])
    print(wikiPage.title)
    wikiSummary = str(wikiPage.summary)
    return wikiSummary

#SPEAKS THE TEXT
def speak(text, rate=120):
    engine.setProperty('rate', rate) 
    engine.setProperty('pitch', 1000)
    engine.say(text)
    engine.runAndWait()


#MAIN LOOP
if __name__ == '__main__':
    speak('SYSTEMS READY', 120)

    while True:
        query = parseCommand().lower().split()


        if query[0] == 'thank':
            speak('I am here to serve you, Your welcome David')

        if query[0] == 'fuck':
            speak('Nah fuck you too')
        
        if query[0] == 'activate':
            speak('Activating...')


        if query[0] == 'hello':
            speak("Hello David")
            
            
        if query and query[0] == activationWord:
            query.pop(0)
            
            #TESTS
            
            if query:
                if query[0] == 'say':
                    if 'hello' in query:
                        speak('I LOVE YOU CHARLES')
                    else:
                        query.pop(0)  # Remove 'say'
                        speech = ' '.join(query)
                        speak(speech)

                #Music Play
                if query[0] == 'play':
                    kit.playonyt(query)
                            
                # Abrir una URL en el navegador predeterminado
                if query[0] == 'open' or query[0] == 'go' and query[1] == 'to':
                    speak("Opening...")
                    query = ' '.join(query[1:])
                    webbrowser.open(query)

                if query[0] == 'time':
                    print(get_current_datetime())
                    speak(get_current_datetime())

                if query[0] == 'please':
                        speak("Let me see what I can find")
                        query = ' '.join(query[1:])
                        response = get_openai_response(query)
                        print(response)
                        speak(response)
                    
                    
                #Wikipedia
                if query[0] == 'Wikipedia':
                    query = ' '.join(query[1:])
                    speak('Querying the universal databank')
                    try:
                        result = search_wikipedia(query)
                        speak(result)
                    except Exception as e:
                        print(f"Error querying Wikipedia: {e}")

                    
                if query[0] == 'kill':
                    speak('Autodestruction Completed, I LOVE YOU Poty')
                    break
                
                