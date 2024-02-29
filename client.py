"""Script to be executed on a client system"""

import socket
from dotenv import dotenv_values
import argparse
import pyfiglet
out=pyfiglet.figlet_format("CLIENT",font="rectangles")

class Client:
    def __init__(self): #initialisation constructor to get values from .env
        config=dotenv_values(".env")
        self.server_ip=config["SERVER_IP"]
        self.port=int(config["PORT"])
        self.host_name=socket.gethostname()
        self.host_ip=socket.gethostbyname(self.host_name)
        
    def contact_server(self,num,msg_list):#Establishing connection with the server and interacting with it
        client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            client.connect((self.server_ip,self.port))
            
            for i in range(num):
                 print(f"{self.host_ip}@client > {msg_list[i]} ")
                 client.send(msg_list[i].encode("utf-8")[:1024])

                 response=client.recv(1024) 
                    
                 response=response.decode("utf-8")
                 print(f"{self.server_ip}@server > {response}")
            client.close()
            print("Connection to the server ended!!!")
        except Exception as e:
            client.close()
            print(e)
            print("Could not connect to the server!!!")
            exit(0)
        
                    
def parse_message(sentence): 
    return sentence.split(';')
#config arguments while executing on the terminal
parser =argparse.ArgumentParser(description="Client 1.1",usage="client.py <flags>")
parser._print_message(out)
parser.add_argument("-n","--number",type=int,default=1,help="Number of messages to be sent.")
parser.add_argument("-m","--message", type=parse_message,help="Mulitiple messages to be sent separated by semicolon",default=None)

args=parser.parse_args()

number=args.number
message=args.message
if message == None:
    message=["ping"]*number
if len(message)<number:
    for i in range(number-len(message)):
        message.append("Ping")
ob=Client()
ob.contact_server(number,message)
