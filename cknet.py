import socket

def checknet():
    IPaddress = socket.gethostbyname(socket.gethostname())
    if IPaddress == "127.0.0.1":
      # print("No Internet connected")
       return False
    else:
       # print(IPaddress)
        return True
        


if __name__ == "__main__":
    checknet()
    
