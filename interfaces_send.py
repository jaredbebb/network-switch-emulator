#### Dependencies
# Python 3.7.4rc1
# scapy==2.4.5
####

from ptp_messages import PTPAnnounce

from scapy import interfaces
from scapy.all import *

# print available network interfaces
interfaces.show_interfaces()

ethernet_interface = "Intel(R) Ethernet Connection I218-LM"

# create Ethernet socket
socket = conf.L2socket(iface=ethernet_interface)

ether_layer = b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x88\xf7'

ptp_announce = PTPAnnounce()
pkt = ether_layer + ptp_announce.pack_message()
raw_pkt = Raw(pkt)
print(raw_pkt)

import time

while(1):
    socket.send(raw_pkt)
    print("sent packet")
    time.sleep(1)