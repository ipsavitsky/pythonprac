def fib(m, n):
    ctr = 2
    prev1 = 1
    prev2 = 1
    last_num = 0
    while ctr <= n:
        last_num = prev1 + prev2 
        if ctr >= m:
            yield last_num
        prev2 = prev1
        prev1 = last_num
        ctr += 1


a, b = eval(input())
for i in fib(a, b):
    print(i)