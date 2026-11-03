import socket

def countLetters(message) : 
    count = 0
    for letter in message : 
        if letter == "s" :
            count += 1

    return count

serverPort = 12000

# we create the server socket
# it has the same params as the client of course
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# the socket bind takes a tuple as an arg. and not two args
# this line binds : assings the port number to the server socket
serverSocket.bind(('', serverPort))

print("The server is ready to receive!")

while True : 
    # when a packet arrives at the server's socket
    # the packet's data is put into the message var, and the sender address into the clientAddress
    message, clientAddress = serverSocket.recvfrom(2048)
    
    # never forget to decode before doing any action
    # and encoding before sending it  
    modifiedMessage = f"There is {countLetters(message.decode())} S letters in your sentence"

    # this attaches the client address to the message and sends the resulting packet to the server's socket
    # letting udp do its job to transport it to clientAddress
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)



