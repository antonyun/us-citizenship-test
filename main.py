import json
from gtts import gTTS
import random
import os

f = open('questions.json')

questions = json.load(f)

language = 'en'

def convertToSpeech(text):
    myobj = gTTS(text=text, lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system("ffplay -autoexit welcome.mp3 > /dev/null 2> /dev/null")

for i in range(10):
    num = (int) (random.random() * len(questions))
    convertToSpeech(f'Question {i + 1}')
    convertToSpeech(questions[num])
