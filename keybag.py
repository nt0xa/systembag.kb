# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class Keybag(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.data = self._root.Data(self._io, self, self._root)
        self.sign = self._root.Sign(self._io, self, self._root)

    class Tag(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = (self._io.read_bytes(4)).decode(u"ascii")
            self.length = self._io.read_u4be()
            _on = self.length
            if _on == 4:
                self.value = self._io.read_u4be()
            elif _on == 8:
                self.value = self._io.read_u8be()
            else:
                self.value = self._io.read_bytes(self.length)


    class Data(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.tag = self._io.ensure_fixed_contents(b"\x44\x41\x54\x41")
            self.length = self._io.read_u4be()
            self.header = self._root.Header(self._io, self, self._root)
            self.keys = [None] * (10)
            for i in range(10):
                self.keys[i] = self._root.Key(self._io, self, self._root)



    class Key(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.tags = [None] * (5)
            for i in range(5):
                self.tags[i] = self._root.Tag(self._io, self, self._root)



    class Sign(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.tag = self._io.ensure_fixed_contents(b"\x53\x49\x47\x4E")
            self.length = self._io.read_u4be()
            self.body = self._io.read_bytes(self.length)


    class Header(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.tags = [None] * (10)
            for i in range(10):
                self.tags[i] = self._root.Tag(self._io, self, self._root)




