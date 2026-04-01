import time
import speech_recognition as sr
import eel
import edge_tts
import pygame
import tempfile
import os
import asyncio

async def _synthesize(text, path):
    communicate = edge_tts.Communicate(text, voice="hi-IN-SwaraNeural")
    await communicate.save(path)

def speak(text):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as f:
        tmp_path = f.name
    asyncio.run(_synthesize(text, tmp_path))
    pygame.mixer.init()
    pygame.mixer.music.load(tmp_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.wait(100)
    pygame.mixer.quit()
    os.remove(tmp_path)

@eel.expose
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        eel.DisplayMessage('Listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=10, phrase_time_limit=6)
    
    try:
        print('Recognizing...')
        eel.DisplayMessage('Recognizing...')
        query = r.recognize_google(audio, language='en')
        print(f'User said: {query}')
        #speak(query)
        time.sleep(2)
        eel.DisplayMessage(query)
        
        

    except Exception as e:
        return ""
    
    return query.lower()

# text = takeCommand()
# speak(text)
@eel.expose
def allCommands():
    query = takeCommand()
    print(query)

    if 'open' in query:
        from engine.features import openCommand
        openCommand(query)
    elif 'on youtube' in query:
        from engine.features import PlayYoutube
        PlayYoutube(query) 
    elif 'kaise ho' in query:
        speak(f" Aapne kaha : {query}")
        speak("Main badhiya hu Satyam ji. Aap kaise ho?")
    elif 'kya kar rahi ho' in query:
        speak(f" Aapne kaha : {query}")
        speak("Main aapke liye kaam kar rhi hu. Aap mujhe koi bhi command de sakte ho.")
    else:
        speak(f" Aapne kaha : {query}")
        
    eel.ShowHood()

    