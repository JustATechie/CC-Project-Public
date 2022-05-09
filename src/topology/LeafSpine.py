import sys

from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info, debug, error
from mininet.link import TCLink
from mininet.topo import Topo


class LeafSpine(Topo):
    def __init__(self, loglevel):
        # a logging level of 1 is debug!
        if loglevel == 1:
            print("Creating Leaf-Spine topology!\n")

        Topo.__init__(self)

        # Right node switch "subnet"
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        # right "subnet" hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')

        # right most switch "subnet" links
        self.addLink(s1, s2)

        # right most "subnet" host links
        self.addLink(s2, h1)
        self.addLink(s2, h2)
        self.addLink(s2, h3)
        self.addLink(s2, h4)

        # middle switch "subnet"
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')

        # middle-right "subnet" hosts
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')
        h8 = self.addHost('h8')

        # middle-left "subnet" hosts
        h9 = self.addHost('h9')
        h10 = self.addHost('h10')
        h11 = self.addHost('h11')
        h12 = self.addHost('h12')

        # middle switch "subnet" links
        self.addLink(s3, s4)
        self.addLink(s3, s5)

        # middle-right "subnet" host links
        self.addLink(s4, h5)
        self.addLink(s4, h6)
        self.addLink(s4, h7)
        self.addLink(s4, h8)

        # middle-left "subnet" host links
        self.addLink(s5, h9)
        self.addLink(s5, h10)
        self.addLink(s5, h11)
        self.addLink(s5, h12)

        # left most switch "subnet"
        s6 = self.addSwitch('s6')
        s7 = self.addSwitch('s7')

        # left most subnet hosts
        h13 = self.addHost('h13')
        h14 = self.addHost('h14')
        h15 = self.addHost('h15')
        h16 = self.addHost('h16')

        # left most switch "subnet" links
        self.addLink(s6, s7)

        # left most subnet host links
        self.addLink(s7, h13)
        self.addLink(s7, h14)
        self.addLink(s7, h15)
        self.addLink(s7, h16)

        # cross subnet links
        self.addLink(s1, s4)
        self.addLink(s1, s5)
        self.addLink(s1, s7)

        self.addLink(s3, s2)
        self.addLink(s3, s7)

        self.addLink(s6, s2)
        self.addLink(s6, s4)
        self.addLink(s6, s5)



topos = {'LeafSpine': LeafSpine}


