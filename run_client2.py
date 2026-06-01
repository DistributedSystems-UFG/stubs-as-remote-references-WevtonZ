import pickle
from client   import *
from dbclient import *
from constRPC import *

if __name__ == "__main__":
    c2   = Client(PORTC2)                 # create client
    data = c2.recvAny()                   # block until stub is received
    dbC2 = pickle.loads(data)             # deserialize the stub
    dbC2.appendData('Client 2')           # append data to same remote list
    print(dbC2.getValue())                # print the list contents
    c2.sendTo(HOSTS, PORTS, [STOP])       # tell server to stop