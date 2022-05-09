import sys

# from src.setup import LogLevel

# from src.setup.LogLevel import *

from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info, debug, error, warning
from mininet.link import TCLink
from mininet.topo import Topo


# Note: if we called LogLevel or tried to call any outside function, mininet will fail to add hosts and switches!
#       This is why we must do simple print statements with if/else hubs for logging!

class TestTopo(Topo):
    def __init__(self, loglevel):
        # a logging level of 1 is debug!
        if loglevel == 1:
            print("Creating Test topology!\n")

        Topo.__init__(self)

        # add level 3 switches
        s1 = self.addSwitch('s1')

        # add level 2 switches
        s2 = self.addSwitch('s2')

        # add all hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        self.addLink(s1, s2)

        self.addLink(s2, h1)
        self.addLink(s2, h2)


topos = {'TestTopo': TestTopo}
