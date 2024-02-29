import socket
from dotenv import dotenv_values
from firewall import Firewall
import time
import datetime
import argparse
import pyfiglet
out=pyfiglet.figlet_format("SERVER",font="rectangles") 
class Server:
    def __init__(self,max_req,sleep_time,maxexceed):
        config=dotenv_values(".env")
        self.server_ip=config["SERVER_IP"]
        self.port=int(config["PORT"])
        self.max_req=max_req
        self.req_count=1
        self.limit_exceed_count=0
        self.maxexceed=maxexceed
        self.sleep_time=sleep_time
        self.event=""

    def limit_reset(self):
            self.req_count=1
            self.firewall_object.request_limit_updation(self.client_ip,self.req_count,self.limit_exceed_count)
    
    def assess_validity(self,white,black):
        if black:
            self.event=f"Firewall Alert : Request from black-listed IP: {self.client_ip}"
            self.firewall_object.trace_comm_info(self.client_ip,self.server_ip,self.event,datetime.datetime.now())
            print(f"Firewall Alert : Request from black-listed IP: {self.client_ip}")
            self.client_socket.send("Firewall prevented the request!".encode("utf-8"))
            self.client_socket.close()
            self.event=f"Firewall Intrusion Acknowledgement"
            self.firewall_object.trace_comm_info(self.server_ip,self.client_ip,self.event,datetime.datetime.now())
            return False
        
        if not white:
            self.event=f"Firewall Alert : Request from unknown IP: {self.client_ip}"
            self.firewall_object.trace_comm_info(self.client_ip,self.server_ip,self.event,datetime.datetime.now())
            print(f"Firewall Alert : Request from unknown IP: {self.client_ip}")
            self.client_socket.send("Firewall prevented the request!".encode("utf-8"))
            self.client_socket.close()
            self.event=f"Firewall Intrusion Acknowledgement"
            self.firewall_object.trace_comm_info(self.server_ip,self.client_ip,self.event,datetime.datetime.now())
            return False
        return True
    def run_req_room(self):
        self.server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server.bind((self.server_ip,self.port))
        self.server.listen(1)
        self.firewall_object=Firewall()
        print(f"Listening on {self.server_ip}:{self.port}....")

        while True:
            self.client_socket,client_address=self.server.accept()
            self.client_ip=client_address[0]     
            white_valid=self.firewall_object.check_whitelisted_ip(self.client_ip)
            black_valid=self.firewall_object.detect_blacklisted_ip(self.client_ip)
            validity=self.assess_validity(white_valid,black_valid)
            self.firewall_object.request_limit_updation(self.client_ip,self.req_count,self.limit_exceed_count)
            try:
                while True and validity:

                    request=self.client_socket.recv(1024)
                    if not request:
                        print(f"Connection from {self.client_ip} closed by the client.")
                        break
                    self.event=f"Message sent by client"
                    self.firewall_object.trace_comm_info(self.client_ip,self.server_ip,self.event,datetime.datetime.now())

                    read_request_limit_exceeded=self.firewall_object.read_request_limit(self.client_ip)>self.max_req

                    if read_request_limit_exceeded and self.firewall_object.read_exceed_count(self.client_ip)+1>self.maxexceed:
                        self.client_socket.send(f"Request Rate limit Exceeded!!! IP:{self.client_ip} has been black-listed by the firewall!".encode("utf-8"))
                        self.event=f"Firewall black_listed an IP"
                        self.firewall_object.trace_comm_info(self.server_ip,self.client_ip,self.event,datetime.datetime.now())
                        self.firewall_object.blacklist_the_client(self.client_ip)
                        print(f"{self.server_ip}@server > Request Rate limit Exceeded!!! IP:{self.client_ip} has been black-listed by the firewall!")                        
                        self.limit_exceed_count+=1
                        break
                    if read_request_limit_exceeded:
                        self.client_socket.send(f"Request Rate limit Exceeded!!! Wait for {self.sleep_time} seconds".encode("utf-8"))
                        self.event=f"Request Rate limit Exceeded"
                        self.firewall_object.trace_comm_info(self.server_ip,self.client_ip,self.event,datetime.datetime.now())
                        print(f"{self.server_ip}@server > Request Rate limit Exceeded!!! Wait for {self.sleep_time} seconds")                        
                        time.sleep(self.sleep_time)
                        self.limit_exceed_count+=1
                        self.limit_reset()
                        continue

                    request=request.decode("utf-8")
                    self.client_socket.send("Acknowledged.".encode("utf-8"))
                    self.event=f"Message sent by server"
                    self.firewall_object.trace_comm_info(self.server_ip,self.client_ip,self.event,datetime.datetime.now())
                    self.req_count+=1
                    self.firewall_object.request_limit_updation(self.client_ip,self.req_count,self.limit_exceed_count)
                    print(f"{self.client_ip}@client > {request}") 
                    print(f"{self.server_ip}@server > Acknowledged.")
                     
                self.req_count=1
                self.limit_exceed_count=0
                self.firewall_object.request_limit_updation(self.client_ip,self.req_count,self.limit_exceed_count)
                self.client_socket.close()
                print("Connection to client closed!!")
            except Exception as e:
                print(e)
                print("Error while establishing connection with client.")
            


parser =argparse.ArgumentParser(description="Server 1.1",usage="server.py <flags>")
parser._print_message(out)
parser.add_argument("-r","--maxreq",type=int,default=10,help="Maximum requests the firewall allows the client to send at a time.")
parser.add_argument("-s","--sleeptime",type=float,default=20.0,help="Waiting time, if the request rate exceeds.")
parser.add_argument("-me","--maxexceed",type=int,default=2,help="Maximum times the firewall allows a client to exceed the request rate limit.")
args=parser.parse_args()
max_req=args.maxreq
sleeptime=args.sleeptime
maxexceed=args.maxexceed
obj=Server(max_req,sleeptime,maxexceed)
obj.run_req_room()
