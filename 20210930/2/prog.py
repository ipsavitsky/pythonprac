a, b = eval(input())
print([i for i in range(a, b) if len(
    [k for k in range(2, int(i**0.5)+1) if i % k == 0]) == 0])
