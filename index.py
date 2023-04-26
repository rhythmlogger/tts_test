from gtts import gTTS


def speak(text):
    tts = gTTS(text=text, lang='ko')
    tts.save('voice/1682397973669.mp3')

# readline_test.py
f = open("C:/workspace/T20230425/tts_test/log/1682397973669.txt", 'r')
line = f.readline()
f.close()

speak(line)
