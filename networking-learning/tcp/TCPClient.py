import socket

serverName = 'localhost'
serverPort = 12000

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# this line initiates a tcp connection between the client and server,
# then the three way handshake is performed and a tcp connection is established
clientSocket.connect((serverName, serverPort))

sentence : str = input("Input lowercase sentence: ")

# we don't need to specify the server address, we already created a tcp connection between the client and the server
# all we need is to send the data and receive it
clientSocket.send(sentence.encode())

modifiedSentence : bytes = clientSocket.recv(1024)

print(f"From Server: {modifiedSentence.decode()}")

# this line closes the socket, hence the tcp connection
clientSocket.close()