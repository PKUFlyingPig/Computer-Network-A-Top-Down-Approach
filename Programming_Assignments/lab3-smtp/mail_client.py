from socket import *
msg = "\r\n I love computer networks!" 
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver 
#mailserver = ("148.163.153.234", 25)
mailserver = ("162.105.129.99", 25)

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)
recv = clientSocket.recv(1024).decode() 
print(recv)
if recv[:3] != '220':
	print('220 reply not received from server.')

# Send HELO command and print server response. 
heloCommand = 'HELO zhongyinmin@pku.edu.cn\r\n' 
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode() 
print(recv1)
if recv1[:3] != '250':
	print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
mailFrom = "MAIL FROM: zhongyinmin@pku.edu.cn\r\n"
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '250':
	print('MAIL FROM error : 250 reply not received from server.')


# Send RCPT TO command and print server response.
# Fill in start
# Fill in end

# Send DATA command and print server response.
# Fill in start
# Fill in end

# Send message data.
# Fill in start
# Fill in end

# Message ends with a single period.
# Fill in start
# Fill in end

# Send QUIT command and get server response.
# Fill in start
# Fill in end