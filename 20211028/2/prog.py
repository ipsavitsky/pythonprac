import itertools
def slide(seq, n):
    ret = 0
    while ret != None:
        first, second = itertools.tee(seq)
        yield from itertools.islice(first, n)
        ret = next(second, None)
        seq = second

import sys
exec(sys.stdin.read())
