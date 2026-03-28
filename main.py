import subprocess
import eel
from engine.features import *
from engine.command import *
eel.init('www')

playAssistantSound()
subprocess.Popen(['start', 'chrome.exe', '--app=http://localhost:8000/index.html'], shell=True)
eel.start('index.html', mode=None, host='localhost', block=True)