from mininet.net import Mininet
from mininet.node import RemoteController, Controller, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info, debug
from mininet.link import TCLink
import time
from time import sleep
import os
import subprocess
import sys

from mininet.topo import Topo
from mininet.util import dumpNodeConnections

# Should we clean each time we run?
cleanBool = False

# BEFORE YOU RUN, PLEASE MAKE SURE TO UPDATE YOUR PATH TO POX
pathToPox = '/home/justatechie/pox/pox.py'

# ALTERNATIVELY, YOU CAN JUST RUN POX SEPARATELY!
# IF DOING THIS, PLEASE SET THE FOLLOWING VARIABLE TO FALSE AND UPDATE THE IP/PORT IF DIFFERENT
poxBool = False
poxIP = '127.0.0.1'
poxPort = 6633

# Class for our linear topology
class LinearTopo(Topo):
    def build(self):
        # performance parameters
        linkParameters = dict(bw=15)

        info('*** Adding hosts\n')
        h1 = self.addHost('h1', isNameSpace=False)
        h2 = self.addHost('h2', isNameSpace=False)

        info('*** Adding switches\n')
        s1 = self.addSwitch('s1')

        # Each link is given 10mb/s, a delay of 10ms, 2% loss, and a 50 packet queue.
        info('*** Adding links\n')
        self.addLink(s1, h1)
        self.addLink(s1, h2, **linkParameters)



def buildTopo(net):
	c0 = net.addController('c0', controller=RemoteController, ip=poxIP, port=poxPort)

	h1 = net.addHost('h1')
	h2 = net.addHost('h2')

	s1 = net.addSwitch('s1')

	net.addLink(s1,h1)
	net.addLink(s1,h2)

	return net


# function that will create and return our remote controller
def createRemoteController():
    info('*** Adding Remote Controller\n')
    c0 = RemoteController(name='c0', ip=poxIP, port=poxPort, link=TCLink)
    return c0


# function that will take in our generated topo and controller and create a mininet object
def createNet():
    info('*** Creating network\n')
    net = Mininet(autoSetMacs=True)
    return net


# function that will start our mininet instance
def startNet(net):
    info('*** Starting network\n')
    net.start()


# function that will start the CLI for mininet
def startCLI(net):
    info('*** Running CLI\n')
    CLI(net)


# function that will stop our mininet instance
def stopNet(net):
    info('*** Stopping network\n')
    net.stop()


# function that will run a simple ping test
def simpleTest(net):
    print("Testing network connectivity")
    net.pingAll()

    hosts = net.hosts

    h1 = hosts[0]
    h2 = hosts[1]

    print("Testing TCP Bandwidth!")
    h1.cmd('telnet', h2.IP(), '5001')
    print("testing")
    serverbw, _clientbw = net.iperf([h1,h2], seconds=5)
    print("Bandwitdh:" + serverbw)


# function to clean the mininet environment
def clean():
    print("Cleaning Mininet environment, please wait!")
    cleanCommand = 'mn -c >/dev/null 2>&1'
    result = os.system(cleanCommand)
    sleep(7)


# function to start pox, our remote controller.
def startPOX():
    if poxBool:
        print("Starting POX, please wait!")
        poxProcess = subprocess.Popen([pathToPox, 'forwarding.hub'])
        time.sleep(2)
        return poxProcess
    else:
        print("Pox running separately!")
        return -1


# function to stop pox, our remote controller
def stopPOX(poxProcess):
    if poxBool:
        print("Shutting down POX!")
        poxProcess.terminate()


# stop both mininet and our pox controller
def stopAll(net, pox):
    stopNet(net)
    stopPOX(pox)


# startup function that setups and initializes Mininet environment.
def startup(argument):

    if(cleanBool):
        clean()

    poxProcess = startPOX()

    # setLogLevel('info')

    #ourTopo = LinearTopo()
    #ourController = createRemoteController()

    # create the net object with our topo and controller
    ourNet = createNet()

    ourNet = buildTopo(ourNet)

    startNet(ourNet)
    if argument == 2:
        startCLI(ourNet)

    return ourNet, poxProcess


if __name__ == '__main__':
    argument = int(sys.argv[1])

    ourNet, poxProcess = startup(argument)

    if argument == 1:
        simpleTest(ourNet)

    stopAll(ourNet, poxProcess)

