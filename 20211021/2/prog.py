import math
funcs = dict()
while True:
    a = input()
    bits = a.split()
    if a[0] == ':':
        funcs[bits[0][1:]] = lambda x: eval(bits[2].split(bits[1])[:-1])
    elif a[0] == 'quit':
        print(len(funcs))
        quit()
    else:
        bts = a.split()
        print(funcs)
        print(bts)
        print(funcs(funcs[bts[0]](bts[1])))
        t = eval(funcs[bts[0]](bts[1]), math.__dict__)
        print(t)
