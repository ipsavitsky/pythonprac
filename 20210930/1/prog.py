l = [int(x) for x in input().split(',')]

for i in range(len(l) - 1):
    for j in range(i, len(l) - 1):
        if (l[j]*l[j] % 100) > (l[j + 1]*l[j + 1] % 100):
            l[j], l[j + 1] = l[j + 1], l[j]

# l.sort(key=lambda x: (x**2) % 100)

print(l)
