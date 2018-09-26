from gtts import gTTS 
import os 
  
mytext = 'Learning how to convert text to speech!'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("welcome.mp3") 