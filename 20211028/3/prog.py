import itertools
print(*sorted(filter(lambda x: x.count('TOR') == 2, map(''.join, itertools.product('TOR', repeat=int(input()))))))
