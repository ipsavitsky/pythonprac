from string import ascii_lowercase


class Alpha:
    from string import ascii_lowercase
    __slots__ = list(ascii_lowercase)

    def __init__(self, **kwargs):
        for arg in kwargs.items():
            setattr(self, arg[0], arg[1])

    def __str__(self):
        for letter in ascii_lowercase:
            if getattr(self)

alp = Alpha(c=10, z=2, a=42)
alp.e = 123
print(alp)
