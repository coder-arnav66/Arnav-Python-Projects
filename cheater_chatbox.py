import webbrowser, pyautogui, speech_recognition as sr, time, pyttsx3,os

pt = []                                                        #a list of past chats so that ai can learn from it and reply

try:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")                                  #recognize the first words of user 
        audio = r.listen(source, timeout = 15)
    user = r.recognize_google(audio)
    print(user)
    time.sleep(1)
    webbrowser.open(f"https://chat.openai.com")                   #open chatbox
    time.sleep(7)
    pyautogui.press('escape')                                      #to escape from sign in option
    pyautogui.typewrite(f"In my conversation with my friend,the previous lines he said was/were- {pt}(ignore if empty), now he is saying {user}.. reply what should i say in one line, whithout any other texts by learning from past texts...")
    pyautogui.press("enter")
    pt.append(user)                                                 # to append the first chats of user in a list 

    while True:
        time.sleep(6)
        
        engine = pyttsx3.init()
        engine.setProperty('rate', 179)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)                  #to tell the user that they can continue speakingc (exhaust after being user for 1 time...)
        engine.say("Continue... I am listening. you can continue you conversations and the process will continue in the background. Say quickly after the ai replies. Watch the microphone icon in your taskbar. when it activates, talk! ")
        engine.runAndWait()
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source, timeout = 15)                   #recognizing user for rest of chats     
        user = r.recognize_google(audio)
        pyautogui.typewrite(f"In my conversation with my friend,the previous lines he said was/were- {pt}(ignore if empty), now he is saying {user}.. reply what should i say in one line, whithout any other texts by learning from past texts...")
        pyautogui.press("enter")                                    #sending messages to ai and getting reply by learning from past chats by giving the list created
        time.sleep(3)
        pt.append(user)                                              #adding the rest chats in a list
        os.system('cls')      
except Exception as e:
    from gtts import gTTS
    import os

    
    tts = gTTS("Your chat has ended either because of error or you might have stopped speaking...", lang="en", slow=False)
                                                                      #last message to notify user that he/she has stopped speaking
    
    tts.save("hello.mp3")

    
    os.system("start hello.mp3")  


