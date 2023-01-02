#### Dependencies
# Python 3.7.4rc1
# scapy==2.4.5
####

from scapy.all import *
from ptp_messages import ptp_announce

# IFACES.show() # let’s see what interfaces are available. Windows only
iface = "Intel(R) Ethernet Connection I218-LM"#<<"full iface name">> or <<IFACES.dev_from_index(12)>> or <<IFACES.dev_from_pcapname(r"\\Device_stuff")>>
socket = conf.L2socket(iface=iface)
# socket is now an Ethernet socket


ether_layer = b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x88\xf7'
pkt = ether_layer + ptp_announce
raw_pkt = Raw(pkt)
print(raw_pkt)

import time

while(1):
    socket.send(raw_pkt)
    print("sent packet")
    time.sleep(1)