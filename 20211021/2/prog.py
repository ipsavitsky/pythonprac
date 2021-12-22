from math import *

funcs = dict()


def add_func(fnc_str):
    bits = fnc_str.split()
    funcs[bits[0]] = bits[1:]


calculated = 0
while not (st := input()).startswith("quit"):
    calculated += 1
    if st[0] == ":":
        add_func(st[1:])
    else:
        func, *vars = st.split()
        local_dict = dict()
        for num, var in enumerate(vars):
            local_dict[funcs[func][num]] = eval(var)
        print(eval(funcs[func][-1], globals(), local_dict))


bits = st.split()
print(eval(bits[1]).format(len(funcs) + 1, calculated + 1))
