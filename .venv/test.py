import win32gui
import pyttsx3

engine = pyttsx3.init()
es = engine.say
erw = engine.runAndWait()

def window_enum_handler(hwnd, resultList):
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '':
        resultList.append((hwnd, win32gui.GetWindowText(hwnd)))

def get_app_list(handles=[]):
    mlst=[]
    win32gui.EnumWindows(window_enum_handler, handles)
    for handle in handles:
        mlst.append(handle)
    return mlst

appwindows = get_app_list()
for i in appwindows:
    print(i)
    
hand = win32gui.FindWindow(None, 'VALORANT  ')
print('here: ' + str(hand))

said = 'I am a donkey'
print(said)
es(said)
engine.runAndWait()