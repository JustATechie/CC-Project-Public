import sys

from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info, debug, error
from mininet.link import TCLink
from mininet.topo import Topo


class SuperSpine(Topo):
    def __init__(self, loglevel):
        # a logging level of 1 is debug!
        if loglevel == 1:
            print("Creating Super-Spine topology!\n")

        Topo.__init__(self)


        # Edge/core Leafs
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')



        # Super spine tier
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')

        # MDA links
        self.addLink(s1, s3)
        self.addLink(s1, s4)
        self.addLink(s1, s5)
        self.addLink(s1, s6)

        self.addLink(s2, s3)
        self.addLink(s2, s4)
        self.addLink(s2, s5)
        self.addLink(s2, s6)


        # ZDA Layer - LEFT
        # Spine Switches
        s7 = self.addSwitch('s7')
        s8 = self.addSwitch('s8')

        # Leaf switches
        s9 = self.addSwitch('s9')
        s10 = self.addSwitch('s10')
        s11 = self.addSwitch('s11')

        # ZDA Links
        self.addLink(s7, s9)
        self.addLink(s7, s10)
        self.addLink(s7, s11)

        self.addLink(s8, s9)
        self.addLink(s8, s10)
        self.addLink(s8, s11)

        # ZDA Layer - RIGHT
        # Spine Switches
        s12 = self.addSwitch('s12')
        s13 = self.addSwitch('s13')

        # Leaf switches
        s14 = self.addSwitch('s14')
        s15 = self.addSwitch('s15')
        s16 = self.addSwitch('s16')

        # ZDA Links
        self.addLink(s12, s14)
        self.addLink(s12, s15)
        self.addLink(s12, s16)

        self.addLink(s13, s14)
        self.addLink(s13, s15)
        self.addLink(s13, s16)

        # MDA to ZDA links
        self.addLink(s3, s7)
        self.addLink(s3, s8)
        self.addLink(s3, s12)
        self.addLink(s3, s13)

        self.addLink(s4, s7)
        self.addLink(s4, s8)
        self.addLink(s4, s12)
        self.addLink(s4, s13)

        self.addLink(s5, s7)
        self.addLink(s5, s8)
        self.addLink(s5, s12)
        self.addLink(s5, s13)

        self.addLink(s6, s7)
        self.addLink(s6, s8)
        self.addLink(s6, s12)
        self.addLink(s6, s13)


        # EDA Layer (hosts) - LEFT
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')

        #EDA Layer (hosts) links
        self.addLink(s9, h1)

        self.addLink(s10, h1)
        self.addLink(s10, h2)
        self.addLink(s10, h3)

        self.addLink(s11, h2)
        self.addLink(s11, h3)

        # EDA Layer (hosts) - RIGHT
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')

        # EDA Layer (hosts) links
        self.addLink(s14, h4)

        self.addLink(s15, h4)
        self.addLink(s15, h5)
        self.addLink(s15, h6)

        self.addLink(s16, h5)
        self.addLink(s16, h6)




topos = {'SuperSpine': SuperSpine}


