from random import randrange

guaranteed_num = int(input())

arr = list()

for i in range(0, 9):
    arr.append(randrange(100))

# print(arr)

arr[randrange(9)] = guaranteed_num

print(arr)

