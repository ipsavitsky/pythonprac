num = int(input())
sum = 0
while num > 0:
    sum += num
    if sum > 21:
        break
    num = int(input())
    

print(sum)
