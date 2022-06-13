import os
import binascii
import code
from core.Network import *


#while(len(Network().hpgp) == 0):
#    Network().sniff(eth1)
Network().pcap('PEV.pcap')
for key in Network().hpgp:
    newDict = Network().hpgp[key]
    NMK = newDict['NMK']
#NMK = bytes(NMK).decode('UTF8','replace')
NMK = binascii.hexlify(NMK)
print('plctool -m', NMK.decode())
#os.system('plctool -m ' + NMK.decode())

