def fib(m, n):
    
    if m == 1 or (m == 0 and m == n):
        yield 1
    elif m == 0:
        yield 1
        yield 1
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


import sys
exec(sys.stdin.read())