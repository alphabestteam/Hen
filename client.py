import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 2222

s.connect(("127.0.0.1", port))
massage = input("print your massage")
s.sendall(bytes(massage, "utf-8"))
data = s.recv(1024)
print("reacived back " + str(data))


s.close()
