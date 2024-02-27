import json
class Firewall:
    def __init__(self):
        self.new_inst=0
    def intrusion_detect(self,client_ip)->bool:
        with open("valid_ip.txt","r") as f_read :
            valid_ip_list=[line.strip() for line in f_read.readlines()]
            print(valid_ip_list)
            if client_ip not in valid_ip_list:
                return False
            return True
    def request_limit_updation(self,client_ip,req_count)->bool:
        f_obj=open("rate_limit.json","r") 
        data=[]
        new_bool=True
        try:
            data=json.load(f_obj)
        except Exception as e:
            new_bool=True
            new_data={"client_ip":client_ip,"req_count":req_count}
        for object in data:
            if object["client_ip"]==client_ip:
                object["req_count"]=req_count
                new_bool=False
        if new_bool==True and data:
            new_data={"client_ip":client_ip,"req_count":req_count}
            new_bool=True
        f_obj.close()
        f_obj=open("rate_limit.json","w")
        
        if new_bool:
            data.append(new_data)
        json.dump(data,f_obj)
        f_obj.close()
        
    def read_request_limit(self,client_ip)->int:
        f_obj=open("rate_limit.json","r") 
        data=json.load(f_obj)
        for object in data:
            if object["client_ip"]==client_ip:
                return object["req_count"]
    def trace_comm_info(self,source_ip,dest_ip,event,timestamp):
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
