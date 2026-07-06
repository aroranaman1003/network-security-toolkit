# src/dns.py

import socket


def dns_lookup(host):
    try:
        return socket.gethostbyname(host)
    except socket.gaierror:
        return None