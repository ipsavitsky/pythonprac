#!/usr/bin/env python3
'''
'''
import zlib
from glob import iglob
from os.path import basename, dirname

SHIFT = "  "

for store in iglob(".git/objects/??/*"):
    Id = basename(dirname(store)) + basename(store)

    with open(store, "rb") as f:
        obj = zlib.decompress(f.read())
        header, _, body = obj.partition(b'\x00')
        kind, size = header.split()
    print(Id, kind.decode())
    if kind == b'tree':
        tail = body
        while tail:
            treeobj, _, tail = tail.partition(b'\x00')
            tmode, tname = treeobj.split()
            num, tail = tail[:20], tail[20:]
            print(f"{SHIFT}{tname.decode()} {tmode.decode()} {num.hex()}")
    elif kind == b'commit':
        out = body.decode().replace('\n', '\n' + SHIFT)
        print(f"{SHIFT}{out}")