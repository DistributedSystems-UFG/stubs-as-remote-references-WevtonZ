from server   import *
from constRPC import *

if __name__ == "__main__":
    s = Server(PORTS)
    s.run()
    print("Servidor encerrado")
