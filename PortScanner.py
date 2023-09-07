import nmap
from socket import *
from typing import List

class Scanner:
    def __init__(self, portNumber):
        self.canConnect = False
        self.port = portNumber
    @property
    def canConnect(self):
        return self._canConnect
    
    @canConnect.setter
    def canConnect(self, value):
        self._canConnect = value
    
    @property
    def port(self):
        return self._port
    
    @port.setter
    def port(self, value):
        self._port = value

target = '127.0.0.1'
   
portScanner = nmap.PortScanner() 

fiwareScanners = [Scanner('1026'), Scanner("1883"), Scanner("4041"), Scanner("8666"), Scanner("27017")]

for scanner in fiwareScanners:
    print("testing port: " + scanner.port)
    result = portScanner.scan(target, scanner.port)
    result = result['scan'][target]['tcp'][int(scanner.port)]['state']
    if result == 'open':
        scanner.canConnect = True
    else:
        scanner.canConnect = False
    
        
if all([scanner.canConnect == True for scanner in fiwareScanners]):
    print("fiware software is installed and running")
else:
    print("fiware is not running")




