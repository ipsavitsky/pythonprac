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


print(C().num)
c, d = C(), C()
c.num = d.num = 2
print(c.num+d.num)
c.num = "qwerqwerqwer"
print(c.num+d.num)
d.num = range(10, 1000, 7)
print(c.num+d.num)
