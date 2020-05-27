from gtts import gTTS
import os
try:
    while(True):
        print("THIS IS PYTHON BASED TEXT TO SPEECH CONVERTER:")
        print("ENTER THE TEXT WHICH DO U WANT TO CONVERT:")
        text=input()
        print("NOW ENTER YOUR PREFERRED LANGUAGE(MUST BE IN ABBREVIATED FORM):")
        lang=input()
        speech=gTTS(text=text,lang=lang,slow=False)
        speech.save("test.mp3")
        os.system("start test.mp3")
        print("DO U WANT TO TRY MORE?:YES : NO")
        q=input()
        if q=="NO":
            break
except:
    pass
        
        
