This is a repo creating to learn the basics of networking. I am planning to work bottom-up, starting from tcp, udp and then going up and implementing an http server and increasing the difficulty by creating some challenging software from scratch. 
I am going to start with python at first, so that my whole focus is in the networking area. Once i feel a little comfortable, I'll rewrite the whole thing in C.

I just finished creating a server and client that use udp to transport the packets.
It is an exageration to call them server and client but they do their job simply and great for learning.
so first i started with the client. apart from importing the necessary socket module, i created a client socket that accepts two params, the first one is the family, i used AF_INET which is IPv4, and the second is the type, which in this case is udp: SOCK_DGRAM.
now that we configured the client's socket, we take the desired message that we want to send to the server, in our case is a user input string, we encode it and we send it to the client's socket with the server's address.
it looks something like this clientSocket.sendto(message.encode(), (serverName, serverPort)). notice that the server address is a tuple.
when the packet reaches the server and it processes it and sends it back to the client, we need to see what it sendes to us. 
we do that using the clientSocket.recvfrom(2048). this method returns a tuple of (message, serverAddress) and we capture the message from the server, and print it to the console. do not forget to decode it.

Creating a server is pretty similar to creating a client, except for some details.
First we create the server's socket, using the same procedure as the client.
Second we bind, and that means we assign the port number to the server's socket, you know the same port number that client uses to contact the server.
Then we create an infinite loop in there. we can still not use it, but what server only processes on request and then shuts down? 
Inside that loop is a listener, it listenes and waits for any packet arriving at the serverName:serverPort
once a packet arrives the serverSocket.recvfrom(2048) captures it and returns a tuple (message, clientAddress).
we process the message and then we send the processed message back to the client using serverSocket.sendto(message, clientAddress). 
Notice how the client address is useful here in comparison to the client one where we can just ignore it as we already have the server's address. 

TODO: I still got one problem to understand: that 2048 in the buffer? how does that work? 