import socket
import time
import argparse

<<<<<<< HEAD
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="target ip")
    parser.add_argument("-fp", "--firstport", dest="firstport", help="start port")
    parser.add_argument("-lp", "--lastport", dest="lastport", help="end port")
    return parser.parse_args()

def scanPort(target, firstPort, lastPort):
    print(f"Target IP: {target}")
=======
def scanPort(target, firstPort, lastPort):
    print(f"target IP: {target}")
>>>>>>> ee6f691b3a3367cac759954d6d8f9d9901e009a7
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
<<<<<<< HEAD
    args = main()
    scanPort(args.target, int(args.firstport), int(args.lastport))
=======
    target = input("Enter the IP address of the target: ")
    firstPort = int(input("Enter the start port: "))
    lastPort = int(input("Enter the end port: "))

    scanPort(target, firstPort, lastPort)
>>>>>>> ee6f691b3a3367cac759954d6d8f9d9901e009a7
