#!/bin/pythons3


import sys #allows us to enter command line arguments, among other things 
import socket  
from datetime import datetime 

#Define our target 

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Translate a host name to IPV4 
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <ip>")
    sys.exit()

#Add a pretty banner 

print("." * 50)
print("Scnnning target " + target)
print("Time started: " + str(datetime.now()))
print("." * 50)

try:
    for port in range(50,85):#we run a for-loop for numbers between 50 and 85.
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# s is a connection #AF_INET=IPV4, SOCK_STREAM = my port

        socket.setdefaulttimeout(1) # is a float. in the function is 1 second
        result = s.connect_ex((target,port))# returns error indicator when there is an error in connection, if not it returns a zero.
        print("Checking port {}".format(port))

        if result == 0:
            print("Port {} is open".format(port))

        s.close()# closes the connection




except KeyboardInterrupt:
    print("\n Exiting program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Couldn't connect to server.")
    sys.exit()
    
