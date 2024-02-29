""" Firewall script responsible for blacklisting the IPs and checking intrusions.It also keeps track of the events happening at the server in the form of a trace file. """

import json
class Firewall: 
    def __init__(self):
        self.new_inst=0
    def check_whitelisted_ip(self,client_ip)->bool: # checks whether the client IP is present in whitelist.txt
        with open("whitelist.txt","r") as f_read :
            valid_ip_list=[line.strip() for line in f_read.readlines()]
            if client_ip not in valid_ip_list:
                return False
            return True
    def detect_blacklisted_ip(self,client_ip)->bool: # checks whether the client IP is present in blacklist.txt
        with open("blacklist.txt","r") as f_read :
            invalid_ip_list=[line.strip() for line in f_read.readlines()]
            if client_ip not in invalid_ip_list:
                return False
            return True    
    def request_limit_updation(self,client_ip,req_count,limit_exceeded)->bool: # updates rate_limit.json for tracking the request rates by each IP
        f_obj=open("rate_limit.json","r") 
        data=[]
        new_bool=True
        try:
            data=json.load(f_obj)
        except Exception as e:
            new_bool=True
            new_data={"client_ip":client_ip,"req_count":req_count,"limit_exceeded":limit_exceeded}
        for object in data:
            if object["client_ip"]==client_ip:
                object["req_count"]=req_count
                object["limit_exceeded"]=limit_exceeded
                new_bool=False
        if new_bool==True and data:
            new_data={"client_ip":client_ip,"req_count":req_count,"limit_exceeded":limit_exceeded}
            new_bool=True
        f_obj.close()
        f_obj=open("rate_limit.json","w")
        
        if new_bool:
            data.append(new_data)
        json.dump(data,f_obj)
        f_obj.close()    
    def read_request_limit(self,client_ip)->int: # Reads and returns the request count sent by each IP
        f_obj=open("rate_limit.json","r") 
        data=json.load(f_obj)
        for object in data:
            if object["client_ip"]==client_ip:
                return object["req_count"]
            
    def read_exceed_count(self,client_ip)->int: # Reads and returns the number of times an IP has exceeded the rate limit
        f_obj=open("rate_limit.json","r") 
        data=json.load(f_obj)
        for object in data:
            if object["client_ip"]==client_ip:
                return object["limit_exceeded"]

    def trace_comm_info(self,source_ip,dest_ip,event,timestamp): # Updates the trace file which contains the log events
        data=[]
        f_read=open("trace.json","r")
        try:
            data=json.load(f_read)
            if self.new_inst==0:
                data=[]
        except Exception as e:
            data=[]
        new_data={"source_ip":source_ip,"destination_ip":dest_ip,"timestamp":str(timestamp),"Event":event}
        data.append(new_data)
        f_out=open("trace.json","w")
        json.dump(data,f_out)
        self.new_inst+=1
        f_read.close()
        f_out.close()
    def blacklist_the_client(self,client_ip): # function to blacklist a client IP
        f_read=open("whitelist.txt","r")
        ip_list=[line.strip() for line in f_read.readlines()]
        ip_list.remove(client_ip)
        f_read.close()
        f_write=open("whitelist.txt","w")
        f_write.writelines(ip_list)
        with open("blacklist.txt","a") as f_obj:
            f_obj.writelines(list(client_ip))
    
