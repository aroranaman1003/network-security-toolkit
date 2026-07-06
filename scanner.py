import socket

def get_user_input():
    host = input("Enter host: ")
    port = int(input("Enter port: "))
    return host, port

def scan_port(host, port):
    scanner_socket = socket.socket()
    scanner_socket.settimeout(3)

    result = scanner_socket.connect_ex((host, port))

    scanner_socket.close()

    return result == 0

def main():
    host, port = get_user_input()

    if scan_port(host, port):
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")

if __name__ == "__main__":
    main()