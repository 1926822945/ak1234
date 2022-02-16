import random
from socket import *
import time
tcp_client_socket = socket(AF_INET, SOCK_STREAM)
port = 80
ip = "www.python.org"
tcp_client_socket.connect((ip, port))
send_data = "f@ck"
print("tcp connecting...")
tcp_client_socket.send(send_data.encode("gbk"))
print("start upload")
time.sleep(3)
print("0%")
a = random.randrange(1, 20)
print(str(a) + "%")
time.sleep(2)
b = random.randrange(20, 40)
print(str(b) + "%")
time.sleep(1)
c = random.randrange(40, 60)
print(str(c) + "%")
time.sleep(2)
d = random.randrange(60, 80)
print(str(d) + "%")
time.sleep(1)
e = random.randrange(80, 99)
print(str(e) + "%")
print("100%")
print("!!completed!!")