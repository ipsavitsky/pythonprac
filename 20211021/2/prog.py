from math import *

funcs = dict()
def add_func(fnc_str):
    bits = fnc_str.split()
    print(bits)
    # bits[2] = '('.join(bits[2].split('(')[1].replace(bits[1], 'x'))
    def f(x):
        eval( f'({bits[1]} := {x})')
        print(bits[2])
        return eval(bits[2])
    funcs[bits[0]] = f


while not (st := input()).startswith('quit'):
    if st[0] == ':':
        add_func(st[1:])
    else:
        func, vars = st.split()
        print(funcs[func](vars))

