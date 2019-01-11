#!/usr/bin/env python3
import sys
import os
import re
import plistlib

from argparse import ArgumentParser
from binascii import unhexlify
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend


parser = ArgumentParser(description='Decrypts systembag.kb file')
parser.add_argument('-k', '--key', dest='key', required=True,
                    help='BAG1 key in hex (32 bytes)', metavar='KEY')
parser.add_argument('-i', '--iv', dest='iv', required=True,
                    help='BAG1 iv in hex (16 bytes)', metavar='IV')
parser.add_argument('-o', '--out', dest='out', required=True,
                    help='output file',
                    metavar='OUT')
parser.add_argument('file')
args = parser.parse_args()


key_regex = r'^[a-fA-F0-9]{64}$'
if not re.match(key_regex, args.key):
    print('Invalid key format. Expected %s.' % key_regex)
    sys.exit(1)

iv_regex = r'^[a-fA-F0-9]{32}$'
if not re.match(iv_regex, args.iv):
    print('Invalid iv format. Expected %s.' % iv_regex)
    sys.exit(1)


key = unhexlify(args.key)
iv = unhexlify(args.iv)


try:
    with open(args.file, 'rb') as f:
        plist = plistlib.loads(f.read())
except FileNotFoundError:
    print('File "%s" not found' % args.file)
    sys.exit(1)
except plistlib.InvalidFileException:
    print('File "%s" is not valid plist' % args.file)
    sys.exit(1)
except Exception:
    print('Ivalid file "%s"' % args.file)
    sys.exit(1)


payload = plist['_MKBPAYLOAD']

algorithm = algorithms.AES(key)
mode = modes.CBC(iv)
cipher = Cipher(algorithm, mode, backend=default_backend())
decryptor = cipher.decryptor()
unpadder = padding.PKCS7(algorithm.block_size).unpadder()
keybag = unpadder.update(decryptor.update(payload)
                         + decryptor.finalize()) + unpadder.finalize()


try:
    keybag_plist = plistlib.loads(keybag)
except Exception:
    print('Fail to parse keybag plist')
    sys.exit(1)


try:
    with open(args.out, 'wb') as f:
        f.write(keybag_plist['KeyBagKeys'])
except Exception:
    print('Fail to save result to "%s"' % args.out)
    sys.exit(1)
