from string import ascii_lowercase


class Alpha:
    from string import ascii_lowercase
    __slots__ = list(ascii_lowercase)

    def __init__(self, **kwargs):
        for arg in kwargs.items():
            setattr(self, *arg)

    def __str__(self):
        res = list()
        for letter in ascii_lowercase:
            if (a := getattr(self, letter, None)) is not None:
                res.append(f'{letter}: {a}')
        return ', '.join(res)

class AlphaQ:
    from string import ascii_lowercase

    def __init__(self, **kwargs):
        for arg in kwargs.items():
            setattr(self, *arg)
    
    def __str__(self):
        res = list()
        for letter in ascii_lowercase:
            if (a := getattr(self, letter, None)) is not None:
                res.append(f'{letter}: {a}')
        return ', '.join(res)
    

import sys
exec(sys.stdin.read())
