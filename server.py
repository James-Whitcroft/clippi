import socket

HOST = '127.0.0.1'
PORT = 6666

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(4)
while 1:
  conn, addr = s.accept()
  print('Connected by', addr)
  while 1:
    data = conn.recv(2048).decode()
    if not data:
      break
    print("DATA: " + str(data))
  conn.close()
s.close()