import time, subprocess, re, subprocess
tryit = False
while tryit == False:
    try:
        import mouse
        tryit = True
    except:
        subprocess.Popen("py -m pip install mouse")
        time.sleep(5)
while tryit == False:
    try:
        import keyboard
        tryit = True
    except:
        subprocess.Popen("py -m pip install keyboard")
        time.sleep(5)
# function
def help():
    print("**voici les fonction que vous pouvez utiliser**")
    try: fichier = open('help.txt', 'r')
    except: fichier= open('help.txt', 'w')
    for ligne in fichier:
        print(ligne)
    fichier.close()

def keyboardkill(data):
    while data == True:
        for i in range(150):
            keyboard.block_key(i)

def mousekill():
    while True:
        mouse.move(0, 0, absolute=True)
    
def addToVariableCmdTaskkill(app, function, loop=1):
    i=0
    ret=""
    while i < loop:
        ret = ret+function+" "+app+"&"
        i = i + 1
    return ret

def shortcut(app, function, loop=1):
    i = 0
    ret = ""
    app = " ".join(app.split("§+"))
    if function == "close":
        subprocess.Popen("taskkill /im "+app+".exe /F"+"& taskkill /im cmd.exe /F", shell=True)
    elif function == "cmd":
        ret = subprocess.getoutput(app)
    else:
        subprocess.Popen(addToVariableCmdTaskkill(app, function, loop)+"taskkill /im cmd.exe /F", shell=True)
    time.sleep(0.4)
    return ret

def stopSpaceError(data):
    data = " ".join(re.split(r"\s+", (re.sub(r"^\s+|\s+$", "", data))))
    return data
    
# main
def speed_write(data):
    securiter = "n"
    timer = 0.40
    seq=[]
    write=[]
    i=0
    while i <= (len(data)-1):
        if data[i] != "{":
            write.append(data[i])
            print(data[i])
        else:
            keyboard.write("".join(write))
            temp = len(write)
            time.sleep(0.20+(temp/80))
            write=[]
            while data[i] != "}":
                i = i + 1
                seq.append(data[i])
            del seq[len(seq)-1]
            cmd = "".join(seq)
            cmd = stopSpaceError(cmd)
            x = cmd.split()
            save = x
            loopNumberList = (x[len(x)-1])
            try:
                loopNumberList=loopNumberList.split("*")
                del loopNumberList[0]
                NumberOfLoop = int(loopNumberList[0])
                del save[len(save)-1]
                cmd = save
            except: NumberOfLoop = 1
            if (x[0] in ("open", "start")) and x[1] == "cmd":
                for indice in range (NumberOfLoop):
                    subprocess.check_call( ('start','cmd') , shell=True )
            elif x[0]in ("open", "start"):
                shortcut(x[1], "start", NumberOfLoop)
            elif x[0] in ("close", "stop"):
                shortcut(x[1], "close")
            elif x[0] in ("cmd", "command"):
                print(shortcut(x[1], "cmd"))
            elif x[0] in ("sleep", "pause"):
                try:
                    time.sleep(int(x[1]))
                except:
                    print("error to sleep")
            else:
                for indice in range (NumberOfLoop):
                    keyboard.press_and_release(cmd)
            seq=[]
            if securiter == "o":
                timer = 0.6
            time.sleep(timer)
        i=i+1
    keyboard.write("".join(write))
   
