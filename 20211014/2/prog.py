from math import sin

f = sin


def scale(A, B, a, b, x):
    return (x-A)/(B-A)*(b-a)+a


def print_field(fld):
    for i in fld:
        print(i)


size_x, size_y = 80, 25
A, B = -4, 4
field = ['' for _ in range(size_x+1)]
# print_field(field)
points = [scale(0, size_x+1, A, B, x) for x in range(size_x+1)]
vals = [f(point) for point in points]
min_val, max_val = min(vals), max(vals)
for val in enumerate(vals):
    field[val[0]] = list(int(scale(min_val, max_val, 0, size_x, val[1]))*' '+'*')
    field[val[0]] += [' ']*(size_x - len(field[val[0]]))

field = [[field[j][i] for j in range(len(field))] for i in range(len(field[0]))]
for line in field:
    print(''.join(line))
