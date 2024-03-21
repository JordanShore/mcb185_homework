#!/usr/bin/env python3

#90dust.py by Jordan Shore
#
#Tests argparse, print_enmask adapted from 63dust.py

import argparse
import dogma

parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('-s','--size', type=int, default=20,
	help='window size [%(default)i]')
parser.add_argument('-e','--entropy', type=float, default=1.4,
	help='entropy threshold [%(default).3f]')
parser.add_argument('--lower', action='store_true', help='soft mask')
arg = parser.parse_args()
print('dusting with', arg.file, arg.size, arg.entropy, arg.lower)

dogma.print_enmask(arg.file, arg.size, arg.entropy, arg.lower)