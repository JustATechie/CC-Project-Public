import sys

from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info, debug, error, warning
from mininet.link import TCLink
from mininet.topo import Topo


# function to set the logging level based on passed arguments.
def determine_logging_level(argument):
    if argument == 0:
        setLogLevel('info')
        info('Log level set to info!\n')
    elif argument == 1:
        setLogLevel('debug')
        debug('Log level set to debug!\n')
    elif argument == -1:
        warning('Log level set to warning!\n')
    else:
        error('Invalid logging level!\n')
        exit(3)


def set_logging_level(argument):
    if argument == 0:
        setLogLevel('info')
    elif argument == 1:
        setLogLevel('debug')
    elif argument == -1:
        warning('Log level set to warning!\n')
    else:
        error('Invalid logging level!\n')
        exit(3)


if __name__ == '__main__':
    determine_logging_level(-1)
