#text to speech
import os
from gtts import gTTS
mytext=input('enter any text:')
language='en'
myobj=gTTS(text=mytext,lang=language,slow=False)
myobj.save('welcome.mp3')
os.system('start welcome.mp3')
