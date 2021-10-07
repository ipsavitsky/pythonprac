from math import *


def Calc(s, t, u):
    def wrapper(x, y):
        return eval(u)

    def new_func(x):
        return wrapper(eval(s), eval(t))
    return new_func


frst, scnd, thrd = eval(input())
arg = eval(input())

fn = Calc(frst, scnd, thrd)
print(fn(arg))