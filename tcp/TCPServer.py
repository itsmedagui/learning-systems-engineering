import socket

serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind(("", serverPort))

# the server socket listen for any incoming tcp connections from clients
serverSocket.listen(10)
print("The server is ready to receive!")

while True : 

    # when a client connects to the server welcoming socket, the server creates another socket: connectionSocket dedicated to this particular client
    # 
    connectionSocket, addr = serverSocket.accept()
    sentence : str = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()

    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()