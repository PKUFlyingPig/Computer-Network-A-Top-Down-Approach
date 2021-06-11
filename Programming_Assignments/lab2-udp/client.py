import socket
import time
server_addr = ("localhost", 12000)
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.settimeout(1)
for i in range(10):
	message = f"PING {i} {time.time()}"
	start = time.time()
	clientSocket.sendto(message.encode(), server_addr)
	try:
		response, _ = clientSocket.recvfrom(1024)
	except socket.timeout:
		print("Request timeout!")
		continue
	end = time.time()
	print(f"RTT {i}: {(end - start)*1000:.3f} ms")

