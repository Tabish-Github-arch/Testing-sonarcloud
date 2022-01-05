"""Top-level implementation of the helloworld program."""

import argparse
import sys

import helloworld


parser = argparse.ArgumentParser(
        description='A simple example program to print a friendly greeting.')
parser.add_argument('--version', action='version',
        version='helloworld ' + helloworld.__version__)