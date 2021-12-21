
a = int(input())
bot = a
top = a + 3
while a < top:
	b = bot
	while b < top:
		sum_digit = 0
		num = b * a
		# print(f'b = {b}')
		while num > 0:
			sum_digit += num%10
			num //= 10
		# print(f'sum_digit = {sum_digit}')
		if sum_digit == 6:
			print(f'{a}*{b}=:=)', end=' ')
			b += 1
			continue
		print(f'{a}*{b}={a*b}', end=' ')
		b += 1
	print()
	a += 1

