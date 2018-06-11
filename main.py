import socket, time
def runClient(data, host="165.227.0.215", port=80):
        try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((host, int(port)))
                s.send(data.encode("utf-8"))
                recieved = s.recv(1024)
                s.close()
                return recieved.decode("utf-8")
        except Exception as e:
                print(e)
                return False

__version__ = "1.0.3"
password = "AranMartin"
last = """"""
while True:
    new = runClient(password)
    if new != last:
        print(new)
        last = new
    time.sleep(0.1)
