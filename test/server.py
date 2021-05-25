import socket, time
from threading import Thread 
from socketserver import ThreadingMixIn 

class myThread(Thread): 
    def __init__(self,ip,port, ID): 
        Thread.__init__(self) 
        self.ID = ID
        self.ip = ip 
        self.port = port 
        print ("[+] Nouveau thread démarré pour " + ip + ":" + str(port))
    def run(self):
        while True:
            time.sleep(10)
            con.send("T36TCo".encode())

# Programme du serveur TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
s.bind(('127.0.0.1', 9999))

def MainThread():
    global mythreads, arrayID, con
    mythreads, arrayID = [], []
    ID=0
    while True:
        ID+=1
        s.listen(5) 
        print("Serveur: en attente de connexions des clients TCP ...")  
        (con, (ip,port)) = s.accept() 
        mythread = myThread(ip,port, ID) 
        mythread.start() 
        mythreads.append([mythread, ip, port])
        arrayID.append(ID)
        print(mythreads)
mainThread = Thread(target=MainThread)
mainThread.start()