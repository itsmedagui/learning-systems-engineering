# the socket module forms the basis for all network communications in python
# by including this we'll be able to create sockets within out program
import socket

serverName = "localhost"
serverPort = 12000

# in this line we create the client socket.
# the first parameter AF_INET indicates that the underlying network is using IPv4.
# the second parameter indicates that the socket is of type SOCK_DGRAM, which means it is a UDP socket.
# we are not specifying a port number for the client socket that we just created. the os does this for us.
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# this prints the input question in the terminal and grabs whatever the client enters into the message variable to use later
message = input("Input lowercase sentence: ")

# this is pretty self explanitory. it takes the message, encode it and then send to serverName:serverPort
# encode it: convert the message from string type to byte type.
# TODO: i need to understand how does the message encoding happen.
# the method sendto attaches the destination address to the message and sends the resulting packet into the process's socket: clientSocket
clientSocket.sendto(message.encode(), (serverName, serverPort))

# when a packet arrives from the server, we put the packet data into modifiedMessage and the packet's source address into serverAddress
# we don't need to capture the server address as we already know it, but recvfrom provides it anyway. we can just put a _ in there
# the 2048 is the buffer size
# TODO : look what does a buffer size do, and its role in sending a packet with udp 
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# now we print the message received from the server after decoding it: converting it from bytes to string
print(modifiedMessage.decode())

# this line closes the socket, then the process terminates
# it is important so that a process is not left hanging using resources for nothing
clientSocket.close()