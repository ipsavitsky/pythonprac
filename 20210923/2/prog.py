num = int(input())
sum = 0
while num > 0:
	sum += num
	if sum > 21:
		print(sum)
	break
	num = int(input())
else:
	print(num)
