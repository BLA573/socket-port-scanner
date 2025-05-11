from socket import *
import time
import threading

def scan_port(target, port):
    s = socket(AF_INET, SOCK_STREAM)
    s.settimeout(1) 
    conn = s.connect_ex((target, port)) 
    if conn == 0:  
        print(f"Port {port}: OPEN")
    else:
        print(f"Port {port}: CLOSED")
    s.close()  

def main():
    start_time = time.time()

    ip = input("Enter the IP address or domain name to scan: ")
    try:
        target = gethostbyname(ip) 
        print(f"Starting scan for IP address: {target}")
    except gaierror:
        print("Error: Unable to resolve host.")
        return

    try:
        start_port = int(input("Enter the starting port: "))
        end_port = int(input("Enter the ending port: "))
        if start_port < 1 or end_port > 65535 or start_port > end_port:
            print("Invalid port range. Ports must be between 1 and 65535, and start must be less than end.")
            return
    except ValueError:
        print("Invalid input for ports. Please enter integers.")
        return

    threads = []

    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Time taken to scan: {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
