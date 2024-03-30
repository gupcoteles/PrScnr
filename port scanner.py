import socket
import time

def scanPort(target, firstPort, lastPort):
    print(f"target IP: {target}")
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
    target = input("Enter the IP address of the target: ")
    firstPort = int(input("Enter the start port: "))
    lastPort = int(input("Enter the end port: "))

    scanPort(target, firstPort, lastPort)
