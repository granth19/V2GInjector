import os
import binascii
import code
import multiprocessing
from core.Network import *

def NetworkSniff():
    #Network().sniff(eth1)
    Network().pcap('PEV.pcap')


#while(len(Network().hpgp) == 0):
#    Network().sniff(eth1)
Network().pcap('PEV.pcap')

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=NetworkSniff)
    p1.start()
    while True:
        if len(Network().hpgp) != 0:
            p1.terminate()
            p1.join()
            for key in Network().hpgp:
                newDict = Network().hpgp[key]
                NMK = newDict['NMK']
            #NMK = bytes(NMK).decode('UTF8','replace')
            NMK = binascii.hexlify(NMK)
            print('plctool -M -K', NMK.decode())
            #os.system('plctool -M -K ' + NMK.decode()+ 'local')
            break
