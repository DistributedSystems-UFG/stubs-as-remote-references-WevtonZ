import pickle
from client   import *
from dbclient import *
from constRPC import *

if __name__ == "__main__":
    c1   = Client(PORTC1)                 # create client
    dbC1 = DBClient(HOSTS, PORTS)         # create stub pointing to server
    dbC1.create()                         # create new list on server
    dbC1.appendData('Client 1')           # append some data
    c1.sendTo(HOSTC2, PORTC2, dbC1)       # send stub to other client
