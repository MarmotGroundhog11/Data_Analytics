#! /bin/python3

import sys
import socket
from datetime import datetime

#Defining Target
if len(sys.argv)==2:
    #Traselation of hostname to IPv4
   target = socket.gethostbyname(sys.argv[1])
else :
   print ("invalid")
#Adding Banner
print("-"* 50)   
print (f"scannig {target}")
print (f"time started : " + str(datetime.now()))
print("-"* 50)   

try: 
     for port in range (50,85):
         s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
         s.settimeout(0.5)
         result = s.connect_ex((target,port))
         if result == 0:
                  print (f"port {port} is open")
         s.close()
except KeyboardInterrupt:
       print ("Exiting Program")
       sys.exit()

except socket.gaierror :
       print ("Hostname could not be resolved")
       sys.exit()
       
except socket.error:
       print("Could not connect to server")
       sys.exit()
       
       
       
