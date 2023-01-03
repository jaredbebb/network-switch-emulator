#### Dependencies
# Python 3.7.4rc1
# scapy==2.4.5
####
from ethernet_layer import EthernetLayer
from ptp_layer import PTPAnnounce, PTPSync, PTPFollow_Up

from scapy import interfaces
from scapy.all import *


# print available network interfaces
interfaces.show_interfaces()

ethernet_interface = "Intel(R) Ethernet Connection I218-LM"

# create Ethernet socket
socket = conf.L2socket(iface=ethernet_interface)

# create ethernet layer
ether_layer = EthernetLayer().pack_message()

import time

while(1):
    for ptp_type in [PTPAnnounce(), PTPSync(), PTPFollow_Up()]:
        # create ptp layer
        ptp_layer = ptp_type.pack_message()
        pkt = ether_layer + ptp_layer
        raw_pkt = Raw(pkt)
        socket.send(raw_pkt)
        print(f"sent ptp message type:{ptp_type.messageType}")
        time.sleep(1)