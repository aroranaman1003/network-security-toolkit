import socket

def get_user_input():
    host = input("Enter host: ")
    start_port = int(input("Enter starting port: "))
    end_port = int(input("Enter ending port: "))
    return host, start_port, end_port

def scan_port(host, port):
    scanner_socket = socket.socket()
    scanner_socket.settimeout(3)

    result = scanner_socket.connect_ex((host, port))

    scanner_socket.close()

    return result == 0

def main():
    host, start_port, end_port = get_user_input()
     
    for port in range(start_port, end_port + 1):
        if scan_port(host, port):
            print(f"Port {port} is OPEN")
        else:
            print(f"Port {port} is CLOSED")

if __name__ == "__main__":
    main()