# Collection of tools to decrypt and parse systembag.kb file

## get_bag1

Extracts `BAG1` key and iv from Effaceable Storage. Based on [iphone-dataprotection](https://github.com/dinosec/iphone-dataprotection) sources.

### Build

```
make
CER="<40 character hex string for certificate>" make codesign
```

### Usage

Copy `get_bag1` binary to the device (e.g. to `/usr/local/bin`) and run it:

```shell
$ get_bag1
iv = e859f45ec0a3ab208ec61477b74e92f0
key = 71ebb0dd387647d7b1c4d10161f5f0b622937867ffe437e41a02ccaacfe8ffb2
```

## decrypt_systembag.py

Decrypts `systembag.kb` file using key and iv extracted by `get_bag1`.

### Usage

Copy `systembag.kb` from the device and run:

```sh
$ ./decrypt_systembag.py -k 71ebb0dd387647d7b1c4d10161f5f0b622937867ffe437e41a02ccaacfe8ffb2 -i e859f45ec0a3ab208ec61477b74e92f0 -o example/keybag example/systembag.kb
```

### parse_keybag.py

Parses keybag decrypted by `decrypt_systembag.py`.

### Usage

Just run: 

```sh
$ ./parse_keybag.py example/keybag
HEADER
  VERS = 4
  TYPE = 0
  UUID = cf7591b3dfc64ce8b4c36018fba96374
  HMCK = e0d8a575d2af7d15bcb26de7688d7c84eb9a4711a845b3c5d56b49c94bdc4216f165ecb4ea97ec18
  WRAP = 1
  SALT = a358808b695d260c8a21ec801ce43db3efafecda
  ITER = 50000
  TKMT = 0
  SART = 98
  UUID = 9ab835423fe14b8c99b4be0ae6b066a3
KEYS
  0:
    CLAS = 1
    WRAP = 3
    KTYP = 0
    WPKY = 150dd562e3c6a441a879e154617d758af77553121c2b70114e32f6ad87a5819b375c724adee094ee
    UUID = 9d4e1c3567cc41058b3d2ee381aaa48b
  1:
    CLAS = 2
    WRAP = 3
    KTYP = 1
    WPKY = 0df35185f13495d49596531f38d7114e77134a91c16915a14f2531241a78afc0ae4deeaefd2d5933
    PBKY = 0252ce8f8acc7068e4ca64cab9227035460ed5cef0661818b382e88609b1a908
  2:
    UUID = 6f537c62fd22484095c2836b227a38eb
    CLAS = 3
    WRAP = 3
    KTYP = 0
    WPKY = 055c81e0fbc7eac3eee65e92a64c53178a95a48df6b0fa0d0ed24f3eb6b2cac9105772f6cb32c391
  3:
    UUID = 9136f182f33b46c29499cc253c94a564
    CLAS = 5
    WRAP = 3
    KTYP = 0
    WPKY = c5867706ef5cc9d03b7f098a9f1f583e58397a984a17173e8d8e685fc9d2ecbc8bb3c9d76ed89c71
  4:
    UUID = 4703951420ef4ceca92d3d6e35aceb02
    CLAS = 6
    WRAP = 3
    KTYP = 0
    WPKY = acb3be303c103526aee718633a1bd946720dd128460bf54bcee99408f9ffe281a96cf352eaf5c710
  5:
    UUID = e42e8612890b48c8bee12f7c3f5510f2
    CLAS = 7
    WRAP = 3
    KTYP = 0
    WPKY = 52a6d7f05a62ccf906ce449f26325f518ad468e6d53a98bff309ac89eba088983148bada67e29a36
  6:
    UUID = 34addd5fffcb4b619d377301e49b16d5
    CLAS = 8
    WRAP = 1
    KTYP = 0
    WPKY = 9f2ddbeeb002c9897f1486244cfa5cb948cd13c23d7c480513b8be36f46a11d1
  7:
    UUID = c703f8b157b44418acbb3de1d5f35178
    CLAS = 9
    WRAP = 3
    KTYP = 0
    WPKY = a777da0779ee752fb9d7f0651ed83c7c16945af3723f30d8d82afc26eb076b99220ebffeebf1b53c
  8:
    UUID = a72aa7d9d1ea4ab6ab6a27c89961d4d4
    CLAS = 10
    WRAP = 3
    KTYP = 0
    WPKY = b7ac60ea56917249d094fd21c44728cd77621f566e7ea6538c3475a2b3d43c6061b0fbc320eb7376
  9:
    UUID = 568dfdd2f8ae4edd9ae7f22bba3c9ce2
    CLAS = 11
    WRAP = 1
    KTYP = 0
    WPKY = 44389e92846f2c7bf1294be2fcaf88153638a881197590df03e0303b1af6ac47
```

