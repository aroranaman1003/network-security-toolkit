import socket

'''
target = "google.com"
# port = 443
port=81
'''
target = input("Enter host: ")
port = int(input("Enter port: "))


scanner_socket = socket.socket()
scanner_socket.settimeout(3)

result = scanner_socket.connect_ex((target, port))

if result == 0:
    print(f"Port {port} is OPEN")
else:
    print(f"Port {port} is CLOSED")

scanner_socket.close()