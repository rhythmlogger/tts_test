import os
import time  # time.sleep(5)
from gtts import gTTS

# Specify the folder path
folder_path = 'C:\\Workspace\\t20230425\\tts_test\\log\\'


def loop_test():
    while True:
        time.sleep(3)
        # Check if the folder exists
        if os.path.exists(folder_path):
            # Get a list of files in the folder
            files = os.listdir(folder_path)
            print(f'There are {len(files)} files in the folder:')
            for file in files:
                with open('C:\\Workspace\\t20230425\\tts_test\\log\\'+file, 'r', encoding='utf-8') as f:
                    contents = f.read()
                    if os.path.exists('voice/'+file.replace(".txt", "")+'.mp3'):
                        continue
                    else:
                        print(file)
                        print(contents)
                        tts = gTTS(text=contents, lang='ko')
                        tts.save('voice/'+file.replace(".txt", "")+'.mp3')
        else:
            print(f'The folder {folder_path} does not exist')


loop_test()
