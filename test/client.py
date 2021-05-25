import socket 
 
msg = input("ClientA: Entrez un message ou exit pour sortir:") 
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect(("127.0.0.1", 9999))
while True:
    print(s.recv(1024).decode())
s.close()