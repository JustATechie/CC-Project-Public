import sys

# logging file
#from src.setup.LogLevel import *

# topology files
# from src.topology import FatTree
# from src.topology.FatTree import *
# from src.topology.LeafSpine import *
# from src.topology.SuperSpine import *
# from src.topology.loopless import *
from FatTree import FatTree

# protocol files
# from src.protocols.tcp import *
# from src.protocols.stcp import *
# from src.protocols.mptcp import *
# from src.protocols.dctcp import *

# general imports
from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info, error, debug
from mininet.link import TCLink
from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch, DefaultController
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.cli import CLI
import os
from os import path
from os import mkdir
import random
import time
import sys
import re
import numpy as np

# variables that may need changing
controller_ip = '192.168.239'

small_flow_min = 100  # KBytes = 100KB
small_flow_max = 10240  # KBytes = 10MB
large_flow_min = 10240  # KBytes = 10MB
large_flow_max = 1024*1024*10  # KBytes = 10 GB

# L4 PROTOCOLS
protocol_list = ['--tcp', '']  # udp / tcp
port_min = 1025
port_max = 65536

# IPERF SETTINGS
sampling_interval = '1'  # seconds


# ELEPHANT FLOW PARAMS
elephant_bandwidth_list = ['10M', '20M', '30M', '40M', '50M', '60M', '70M', '80M', '90M', '100M',
                           '200M', '300M', '400M', '500M', '600M', '700M', '800M', '900M', '1000M']

# MICE FLOW PARAMS
mice_bandwidth_list = ['100K', '200K', '300K', '400K', '500K', '600K', '700K', '800K', '900K', '1000K',
                       '2000K', '3000K', '4000K', '5000K', '6000K', '7000K', '8000K', '9000K', '10000K', '1000K']


def random_normal_number(low, high):
    range = high - low
    mean = int(float(range) * float(75) / float(100)) + low
    sd = int(float(range) / float(4))
    num = np.random.normal(mean, sd)
    return int(num)



# function to call on the right topology method to be created.
def determine_topology(argument):
    if argument == 0:
        # fattree()
        return "FatTree"

    elif argument == 1:
        # leafspine()
        return "LeafSpine"

    elif argument == 2:
        # superspine()
        return "SuperSpine"

    elif argument == 3:
        # loopless()
        return "LoopLess"

    elif argument == -1:
        return "TestTopo"

    else:
        error('Invalid topology argument!')
        exit(1)


# function to call on the right protocol to be used.
def determine_protocol(argument):
    if argument == 0:
        #tcp()
        return "TCP"

    elif argument == 1:
        #stcp()
        return "STCP"

    elif argument == 2:
        #mptcp()
        return "MPTCP"

    elif argument == 3:
        #dctcp()
        return "DCTCP"

    else:
        error('Invalid protocol argument!\n')
        exit(2)


def determine_logging_level(argument):
    if argument == 0:
        setLogLevel('info')
        info('Log level set to info!\n')
    elif argument == 1:
        setLogLevel('debug')
        debug('Log level set to debug!\n')
    # elif argument == -1:
        # warning('Log level set to warning!\n')
    else:
        error('Invalid logging level!\n')
        exit(3)


# startup function (main)
def startup():
    clean_command = 'mn -c'
    os.system(clean_command)


    z = -1

    # z is the logging level, call be null
    if len(sys.argv) == 4:
        z = int(sys.argv[3])
        determine_logging_level(z)

    # x is the topology setting
    x = int(sys.argv[1])

    # y is the protocol setting
    #y = int(sys.argv[2])

    topology = determine_topology(x)
    #protocol = determine_protocol(y)

    # command = "sudo -S mn --custom ../topology/" + topology + ".py"

    command = "sudo -S mn --controller=remote,ip=192.168.1.239,port=6653 --mac --switch=ovsk,protocols=OpenFlow13 " \
              "--custom ../topology/" + topology + ".py --topo=" + topology + "," + z.__str__()

    # command = "sudo -S mn --mac --custom ../topology/" + topology + ".py --topo=" + topology + "," + z.__str__()

    # os.system('ls ../topology/')
    os.system(command)


if __name__ == '__main__':
    startup()
