import sys

from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info, debug, error
from mininet.link import TCLink
from mininet.topo import Topo


class FatTree(Topo):
    def __init__(self, loglevel):
        # a logging level of 1 is debug!
        if loglevel == 1:
            print("Creating Fat Tree topology!\n")

        Topo.__init__(self)

        # Right node switch subnet
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')

        # right subnet hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')

        # right most switch subnet links
        self.addLink(s1, s2)
        self.addLink(s2, s4)
        self.addLink(s2, s5)
        self.addLink(s3, s4)
        self.addLink(s3, s5)

        # right most subnet host links
        self.addLink(s4, h1)
        self.addLink(s4, h2)
        self.addLink(s5, h3)
        self.addLink(s5, h4)

        # middle-right switch subnet
        s6 = self.addSwitch('s6')
        s7 = self.addSwitch('s7')
        s8 = self.addSwitch('s8')
        s9 = self.addSwitch('s9')
        s10 = self.addSwitch('s10')

        # middle-right subnet hosts
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')
        h8 = self.addHost('h8')

        # middle-right switch subnet links
        self.addLink(s6, s7)
        self.addLink(s7, s9)
        self.addLink(s7, s10)
        self.addLink(s8, s9)
        self.addLink(s8, s10)

        # middle-right subnet host links
        self.addLink(s9, h5)
        self.addLink(s9, h6)
        self.addLink(s10, h7)
        self.addLink(s10, h8)

        # middle-left switch subnet
        s11 = self.addSwitch('s11')
        s12 = self.addSwitch('s12')
        s13 = self.addSwitch('s13')
        s14 = self.addSwitch('s14')
        s15 = self.addSwitch('s15')

        # middle-left subnet hosts
        h9 = self.addHost('h9')
        h10 = self.addHost('h10')
        h11 = self.addHost('h11')
        h12 = self.addHost('h12')

        # middle-left switch subnet links
        self.addLink(s11, s13)
        self.addLink(s12, s14)
        self.addLink(s12, s15)
        self.addLink(s13, s14)
        self.addLink(s13, s15)

        # middle-left subnet host links
        self.addLink(s14, h9)
        self.addLink(s14, h10)
        self.addLink(s15, h11)
        self.addLink(s15, h12)

        # left most switch subnet
        s16 = self.addSwitch('s16')
        s17 = self.addSwitch('s17')
        s18 = self.addSwitch('s18')
        s19 = self.addSwitch('s19')
        s20 = self.addSwitch('s20')

        # left most subnet hosts
        h13 = self.addHost('h13')
        h14 = self.addHost('h14')
        h15 = self.addHost('h15')
        h16 = self.addHost('h16')

        # left most switch subnet links
        self.addLink(s16, s18)
        self.addLink(s17, s19)
        self.addLink(s17, s20)
        self.addLink(s18, s19)
        self.addLink(s18, s20)

        # left most subnet host links
        self.addLink(s19, h13)
        self.addLink(s19, h14)
        self.addLink(s20, h15)
        self.addLink(s20, h16)

        # cross subnet links
        self.addLink(s1, s7)
        self.addLink(s1, s12)
        self.addLink(s1, s17)

        self.addLink(s6, s2)
        self.addLink(s6, s12)
        self.addLink(s6, s17)

        self.addLink(s11, s3)
        self.addLink(s11, s8)
        self.addLink(s11, s18)

        self.addLink(s16, s3)
        self.addLink(s16, s8)
        self.addLink(s16, s13)



topos = {'FatTree': FatTree}


