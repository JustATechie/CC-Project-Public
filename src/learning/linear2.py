from mininet.link import TCLink
from mininet.net import Mininet
from mininet.node import RemoteController, Controller, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info, debug
import time
import os

from mininet.topo import Topo
from mininet.util import dumpNodeConnections


def createNet():
    debug('*** Creating network\n')
    net = Mininet(autoSetMacs=True)
    return net


def addTopo(net):
    debug('*** Adding hosts\n')
    h1 = net.addSwitch('h1')
    h2 = net.addSwitch('h2')

    debug('*** Adding switches\n')
    s1 = net.addSwitch('s1')

    # Each link is given 10mb/s, a delay of 10ms, 2% loss, and a 50 packet queue.
    debug('*** Adding links\n')
    net.addLink('s1', 'h1')
    net.addLink('s1', 'h2')

    return net


def startNet(net):
    debug('*** Starting network\n')
    net.start()
    return net


def startCLI(net):
    debug('*** Running CLI\n')
    CLI(net)


def stopNet(net):
    debug('*** Stopping network\n')
    net.stop()


def simpleTest(net):
    #print("Dumping host connections")
    #dumpNodeConnections(net.hosts)
    print("Testing network connectivity")
    net.pingAll()

def test():
    debug('*** Creating network\n')
    net = Mininet(autoSetMacs=True, )

    debug('*** Adding Controller\n')
    c0 = net.addController('c0')

    debug('*** Adding hosts\n')
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')

    debug('*** Adding switches\n')
    s1 = net.addSwitch('s1')

    # Each link is given 10mb/s, a delay of 10ms, 2% loss, and a 50 packet queue.
    debug('*** Adding links\n')
    net.addLink('s1', 'h1')
    net.addLink('s1', 'h2')

    debug('*** Starting network\n')
    net.start()

    debug('*** Running CLI\n')
    CLI(net)

    debug('*** Stopping network\n')
    net.stop()



if __name__ == '__main__':
    setLogLevel('info')
    # ourNet = createNet()
    # ourNet = addTopo(ourNet)
    # ourNet = startNet(ourNet)
    # startCLI(ourNet)
    # stopNet(ourNet)

    test()
