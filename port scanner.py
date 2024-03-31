import socket
import time
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="target ip")
    parser.add_argument("-fp", "--firstport", dest="firstport", help="start port")
    parser.add_argument("-lp", "--lastport", dest="lastport", help="end port")
    return parser.parse_args()

def scanPort(target, firstPort, lastPort):
    print(f"Target IP: {target}")
    print(f"Port Range: {firstPort} - {lastPort}")
    print("-" * 40)

    for port in range(firstPort, lastPort + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} open")
        except socket.gaierror:
            print(f"The target's ip cannot be reached.")
        except Exception as error:
            print(f"Error: {error}")
        finally:
            s.close()

if __name__ == "__main__":
    args = main()
    scanPort(args.target, int(args.firstport), int(args.lastport))