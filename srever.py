import socket


def main():
    PORT = 2222
    HOST = '127.0.0.1'
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind((HOST, PORT))

    s.listen()
    print("hen")
    while True:
        conn,addr = s.accept()
        data = conn.recv(1024).decode('utf-8')
        if data:
            print("accept " , str(data))
            conn.sendall(bytes(data.upper().encode('utf-8')))
            s.listen()
        if data == "Stop":
            break
    s.close()


if __name__ == "__main__":
    main()
