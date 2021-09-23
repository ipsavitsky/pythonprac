
a = int(input())
bot = a
top = a + 3
while a < top:
    b = bot
    while b < top:
        sum_digit = 0
        for n in str(a*b):
            sum_digit += int(n)
        if sum_digit == 6:
            print(':=)', end=' ')
            b += 1
            continue
        print(f'{a}*{b}={a*b}', end=' ')
        b += 1
    print()
    a += 1

