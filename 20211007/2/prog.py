def SUB(x, y):
    if type(x) == type([]):
        return [item for item in x if item not in y]
    if type(x) == type(()):
        return tuple([item for item in x if item not in y])
    return x - y

first, second = eval(input())

print(SUB(first, second))
