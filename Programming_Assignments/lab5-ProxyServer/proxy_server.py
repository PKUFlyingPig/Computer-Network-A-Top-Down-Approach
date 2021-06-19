from socket import * 
import sys
if len(sys.argv) <= 1:
	print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
	sys.exit(2)
# Create a server socket, bind it to a port and start listening 
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(('localhost', 6666))
tcpSerSock.listen(5)
while 1:
	# Start receiving data from the client 
	print('Ready to serve...')
	tcpCliSock, addr = tcpSerSock.accept() 
	print('Received a connection from:', addr) 
	message = tcpCliSock.recv(1024).decode()
	print(message)

	# Extract the filename from the given message 
	print(message.split()[1])
	filename = message.split()[1].partition("/")[2] 
	print(filename)
	fileExist = "false"
	filetouse = "/" + filename
	print(filetouse)
	try:
		# Check wether the file exist in the cache 
		f = open(filetouse[1:], "r")
		outputdata = f.read()
		f.close()
		# ProxyServer finds a cache hit and generates a response message 
		tcpCliSock.send("HTTP/1.0 200 OK\r\n".encode()) 
		tcpCliSock.send("Content-Type:text/html\r\n".encode())
		tcpCliSock.send("\r\n".encode())
		for c in outputdata:
			tcpCliSock.send(c.encode())
		print('Read from cache')
	# Error handling for file not found in cache
	except IOError:
		# Create a socket on the proxyserver
		c = socket(AF_INET, SOCK_STREAM)
		hostn = filename.replace("www.","",1) 
		print(hostn)
		try:
			# Connect to the socket to port 80
			c.connect((hostn, 80))
			c.send("GET "+"http://" + filename + "HTTP/1.0\r\n".encode())
			# Create a temporary file on this socket and ask port 80 for the file requested by the client
			fileobj = c.makefile('rb')
			# Read the response into buffer
			for line in fileobj:
				print(line)
			fileobj.close()
			# # Create a new file in the cache for the requested file.
			# # Also send the response in the buffer to client socket and the corresponding file in the cache
			# with open("./" + filename,"wb") as tempFile:
			# 	tempFile.write()
			# # Fill in start.
			# # Fill in end.
		except:
			print("Illegal request")
		else:
			c.close()

	# Close the client and the server sockets
	tcpCliSock.close()
	tcpSerSock.close()
	break
