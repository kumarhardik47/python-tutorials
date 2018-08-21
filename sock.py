import sys
import socket
import uuid

class serverSocket():
    def __init__(self, port_num):
	self.port = port_num

    #Gets ip address
    def getIpAddress(self):
	ip = socket.gethostbyname(socket.getfqdn())
	return ip

    #Gets mac address
    def getMacAddress(self):
	unique_num = uuid.getnode()
	print type(unique_num), unique_num
	mac = hex(unique_num).replace('0X', '')
	mac_address = ':'.join(mac[i : i+2] for i in range(0,11, 2))
	return mac_address	    

    #Gets broadcast address
    def getBradcastAddress(self, ip):
	b = socket.inet_aton(ip)[:3] + b'\xff'
	print "b", b
	brodcast_ip = socket.inet_ntoa(b)
	return brodcast_ip

    def server(self):
	#Create a socket object
	socket_object =socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	#get device details
	ip = self.getIpAddress()
	mac_address = self.getMacAddress()
	brodcast_address = self.getBradcastAddress(ip)

	#Bind Ip and port numbe
	socket_object.bind((brodcast_address, int(self.port)))

	#Queue up 5 request
	socket_object.listen(5)

        #establish a connection
	socket_new_object, address = socket_object.accept()

	message = "Ip of the device : " + ip + "\nMac address : " + mac_address + "\nBrodcast address : " + brodcast_address

	socket_new_object.send(message)
        print socket_new_object.recv(1024)

	#close a conncection
	socket_new_object.close()



if __name__ == '__main__':
    if len(sys.argv) != 2 :
	print "Usage : python server.py port_number"
	sys.exit()

    port = sys.argv[1]
    
    #create object of serverSocket class
    obj = serverSocket(port)
    obj.server()


