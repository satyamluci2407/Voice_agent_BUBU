import eel
import os
from playsound import playsound


def playAssistantSound():
    music_dir = "www\\assets\\audio\\bubu_slow.mp3"
    playsound(music_dir)
    
@eel.expose
def playClickSound():
    music_dir = "www\\assets\\audio\\clickSound.mp3"
    playsound(music_dir)
 