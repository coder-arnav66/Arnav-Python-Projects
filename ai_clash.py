import webbrowser, pyautogui, time, keyboard
print("Welcome to AI clash. Ask a question and get the answer with all AI chatbox...press \'%\' to move to another AI...")

user = input("User: ")
print("Process starting...")
def search(url, so):
    webbrowser.open(url)
    if(so == "yes"):
        time.sleep(7)
        pyautogui.press("escape")
        pyautogui.typewrite(user)
        time.sleep(2)
        pyautogui.press("enter")
    else:
        time.sleep(4)
        pyautogui.typewrite(user)
        time.sleep(3)
        pyautogui.press("enter")


search("https://chatgpt.com", "yes")

while True:
    if keyboard.is_pressed('%'):
        webbrowser.open("https://copilot.microsoft.com")
        time.sleep(5)
        pyautogui.typewrite(user)
        time.sleep(2)
        pyautogui.press("enter")
        break
while True:
    if keyboard.is_pressed('%'):
        search("https://duck.ai", "no")
        break
            
