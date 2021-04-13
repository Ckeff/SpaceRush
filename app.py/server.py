import socket 
import __thread
import sys

server = ""
port = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	server.bind((server, port))
except socket.error as e:
	str(e)

server.listen(2)
print("Waiting for a connection, Server connected")

def threaded_client(conn):

	reply=""
	while True:
		try:
			data = conn.recv(2048)
			reply = data.decode("utf-8")

			if not data:
				print("Disconnected")
				break
			else: 
				print("Received", reply)
				print("Sending", reply)

			conn.sendall(str.encode(reply))
		except:
			break

while True:
	conn, addr = server.accept()
	print("Connected to: ", addr)

	startNewThread(threaded_client, (conn,))