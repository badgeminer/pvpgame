import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = ""
        self.port = 15442
        self.addr = (self.server, self.port)
        #self.p = self.connect()
        self.id = self.connect()
        print(self.id)

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            #return pickle.loads(self.client.recv(2048))
            return self.client.recv(2048).decode("utf-8")
        except:
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)

n = Network()