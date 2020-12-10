import socket
from IPy import IP
from colorama import Fore


class PortScan:

    def __init__(self, target_addr, target_port):
        self.target_addr = target_addr
        self.target_port = target_port

    def scan_target(self):
        for port in range(1, self.target_port):
            self.scan_port(port)

    def check_addr(self):
        try:
            IP(self.target_addr)
            return self.target_addr
        except ValueError:
            return socket.gethostbyname(self.target_addr)

    def scan_port(self, target_port):
        try:
            converted_addr = self.check_addr()
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            sock.connect((converted_addr, target_port))
            try:
                banner = sock.recv(1024).decode('utf8').strip('\n').strip('\r')
                print(f'[*] Open port: = [{Fore.GREEN}{target_port}{Fore.WHITE}] : {banner}')
            except:
                print(f'[*] Open port: [{Fore.GREEN}{target_port}{Fore.WHITE}]')
            sock.close()
        except:
            pass


def main():
    target = input('[+] Enter target address: ')
    ports = int(input('[+] Input amount of ports (100 - first 100 ports): '))

    scanner = PortScan(target, ports)
    scanner.scan_target()


if __name__ == '__main__':
    main()
