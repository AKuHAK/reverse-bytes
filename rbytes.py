#!/usr/bin/env python

"""
A simple python script for reverse the bytes of a file.

Author: Lenin Alevski Huerta Arias
Year: 2018

"""

from __future__ import print_function
import os
import sys
import argparse


def main(arguments):

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('infile', help="Input file",
                        type=argparse.FileType('rb'))
    parser.add_argument('-o', '--outfile', help="Output file",
                        default=sys.stdout, type=argparse.FileType('wb'))

    args = parser.parse_args(arguments)
    byte_list = bytearray(args.infile.read())
    for i in range(len(byte_list)):
        byte_list[i] = int(bin(byte_list[i])[2:].zfill(8)[::-1], 2)

    reversed_contents = bytes(byte_list)
    args.outfile.write(reversed_contents)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
