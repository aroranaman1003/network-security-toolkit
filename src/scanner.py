import socket
from src.dns import dns_lookup

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


def get_user_input():
    host = input("Enter host: ")
    start_port = int(input("Enter starting port: "))
    end_port = int(input("Enter ending port: "))

    return host, start_port, end_port


def scan_port(host, port):

    scanner_socket = socket.socket()
    scanner_socket.settimeout(3)

    try:
        result = scanner_socket.connect_ex((host, port))
        return result == 0

    finally:
        scanner_socket.close()


def run_port_scanner():

    host, start_port, end_port = get_user_input()
    open_ports = 0
    closed_ports = 0
    ip = dns_lookup(host)

    if ip is None:
        print("Host could not be resolved.")
        return

    print(f"\nResolved IP: {ip}")
    print(f"Scanning {host}...\n")

    for port in range(start_port, end_port + 1):

        service = COMMON_PORTS.get(port, "Unknown Service")

        if scan_port(ip, port):
            open_ports+=1
            print(f"Port {port} is OPEN ({service})")
        else:
            closed_ports+=1
            print(f"Port {port} is CLOSED ({service})")

    print(f"\nScan complete. Open ports: {open_ports}, Closed ports: {closed_ports}")