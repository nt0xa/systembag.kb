#!/usr/bin/env python3
from argparse import ArgumentParser
from keybag import Keybag
from binascii import hexlify


def print_tag(tag, indent=''):
    line = '%s%s = ' % (indent, tag.name)
    if type(tag.value) == int:
        line += '%d' % tag.value
    elif type(tag.value) == bytes:
        line += hexlify(tag.value).decode()
    print(line)


parser = ArgumentParser(description='Parse decrypted keybag')
parser.add_argument('file')
args = parser.parse_args()

kb = Keybag.from_file(args.file)

print('HEADER')
for tag in kb.data.header.tags:
    print_tag(tag, indent='  ')

print('KEYS')
for i, key in enumerate(kb.data.keys):
    print('  %d:' % i)
    for tag in key.tags:
        print_tag(tag, indent='    ')
