class Num:
    def __get__(self, obj, cls):
        return getattr(obj, '_val', 0)

    def __set__(self, obj, value):
        if '__len__' in value.__dir__():
            obj._val = len(value)
        elif 'real' in value.__dir__():
            obj._val = value
        
    def __delete__(self, obj):
        obj._val = None


class C:
    num = Num()


import sys
exec(sys.stdin.read())
