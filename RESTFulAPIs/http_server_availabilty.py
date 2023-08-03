#!/usr/bin/env python

import argparse
import socket


def main():
    args = parse_args()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((args.server, int(args.port)))
        sock.settimeout(2)
        sock.send(b"HEAD / HTTP/1.1\r\nHost: " + bytes(args.server, "utf8") + b"\r\nConnection: close\r\n\r\n")
        reply = sock.recv(100)
        sock.shutdown(socket.SHUT_RDWR)
        print(str(reply).split("\\r")[0])
    except socket.timeout:
        print("Timeout reached while establishing a connection with the server")
    except:
        print(f"Can not establish a connection with {args.server}")


def is_valid_port(port):
    if not port.isdigit() or int(port) not in range(1, 65536):
        raise SystemExit(f"Invalid port {port}")
    return port


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--server", required=True, action="store")
    parser.add_argument("--port", type=is_valid_port, default="80", action="store")
    return parser.parse_args()


if __name__ == "__main__":
    main()
