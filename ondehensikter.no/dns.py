import socket

from dnslib import DNSRecord

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(('0.0.0.0', 53))

while True:
    try:
        data, addr = server.recvfrom(4096)
        d = DNSRecord.parse(data)
        print(d.questions[0]._qname)
    except OSError:
        pass