def is_dominated(x, y):
    if x[0] <= y[0] and x[1] <= y[1] and (x[0] < y[0] or x[1] < y[1]):
        return True
    else:
        return False


def Pareto(*args):
    to_delete = []
    for i, first in enumerate(args):
        for second in args[i+1:]:
            if is_dominated(first, second):
                to_delete.append(first)

    return tuple([item for item in args if item not in to_delete])

nums = eval(input())
print(Pareto(*nums))
