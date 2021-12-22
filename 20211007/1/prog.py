def is_dominated(x, y):
    if x[0] <= y[0] and x[1] <= y[1] and (x[0] < y[0] or x[1] < y[1]):
        return True
    else:
        return False


def Pareto(*args):
    to_delete = []
    for first in args:
        for second in args:
            # print(f'checking {first} and {second}')
            if is_dominated(first, second):
                to_delete.append(first)
                continue

    return tuple([item for item in args if item not in to_delete])

nums = eval(input())
print(Pareto(*nums))

