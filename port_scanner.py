
import socket

def scan_ports(host, ports):
    open_ports = []
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.5)
                if sock.connect_ex((host, port)) == 0:
                    open_ports.append(port)
        except:
            continue
    return open_ports
