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
    COMMON_PORTS = {
    20: "FTP Data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP",
    68: "DHCP",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP",
}
     
    for port in range(start_port, end_port + 1):
        if scan_port(host, port):
            if port in COMMON_PORTS:
                print(f"Port {port} is OPEN ({COMMON_PORTS[port]})")
            else:
                print(f"Port {port} is OPEN")
        else:
            if port in COMMON_PORTS:
                print(f"Port {port} is CLOSED ({COMMON_PORTS[port]})")
            else:
                print(f"Port {port} is CLOSED")

if __name__ == "__main__":
    main()