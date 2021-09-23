num = eval(input())
print('A ' + ('+' if num % 2 == 0 and num % 25 == 0 else '-'), end=' ')
print('B ' + ('+' if num % 2 != 0 and num % 25 == 0 else '-'), end=' ')
print('C ' + ('+' if num % 8 == 0 else '-'))