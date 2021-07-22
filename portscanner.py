import socket
from IPy import IP

def scan_port(target,port):
    try:
        sock = socket.socket()
        # sock.settimeout(0.5)
        sock.connect((target, port))
        try:
            banner = get_banner(sock)
            print("[+] Port " + str(port) + " Is Open : " + str(banner.decode().strip("\n")))
        except:
            print("[+] Port " + str(port) + " Is Open")
    except:
        print("[-] Port " + str(port) + " Is Close")

def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)


def scan(target):
    converted_ip = check_ip(target)
    print("\n[-_0] Scanning Target " + str(target) + " :")
    for port in range(1,100):
        scan_port(converted_ip,port)

def get_banner(s):
    return s.recv(1024)

if __name__ == "__main__":
    try:
        print("<== Running PortScanner V.1 ==>\n")
        targets = input("[*] Enter Target/s To Scan(Use , For Multiple Target): ")
        if "," in targets:
            for target in targets.split(","):
                scan(target.strip(" "))
        else:
            scan(targets.strip(" "))
    except KeyboardInterrupt:
        print("[!] Exiting Program")
    finally:
        print("\n[!] Program Finish")