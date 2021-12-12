from functools import wraps

def logging_wrapper(fn):
    @wraps(fn)
    def internal(self, *args, **kwargs):
        print(f'{fn.__name__}: {args}, {kwargs}')
        return fn(self, *args, **kwargs)
    return internal

class dump(type):
    def __new__(cls, name, parents, ns):
        for elem in ns:
            if hasattr(elem[1], '__call__'):
                ns[elem[0]] = logging_wrapper(elem[1])
        return super().__new__(cls, name, parents, ns)

import sys
exec(sys.stdin.read())