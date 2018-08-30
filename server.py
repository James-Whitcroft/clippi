#!/usr/bin/python3

import socket

try:
  fh = open('clip_config.conf', 'r')
  CONFIGS = eval(fh.read())
  fh.close()

  try:
    fh = open(CONFIGS['OUTFILE'], 'a')
    write_flag = 1
  except Exception as err:
    try:
      print('Couldnt open ' + CONFIGS['OUTFILE'] + ' for writing.')
      write_flag = 0
    except Exception as err:
      print('No outfile set.')
      write_flag = 0
      
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind((CONFIGS['HOST'], CONFIGS['PORT']))

  s.listen(4)
  while 1:
    conn, addr = s.accept()
    print('Connected by', addr)
    while 1:
      data = conn.recv(2048).decode()
      if not data:
        break
      print("DATA: " + str(data))
      if write_flag:
        fh.write(str(data))
    conn.close()
  s.close()
  fh.close()

except Exception as err:
  print('No config found.')
