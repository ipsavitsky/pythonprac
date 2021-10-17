lines = [input()]

while True:
    i = input()
    lines.append(i)
    if i[1] == '#':
        break

amnt_of_gas = 0
for i in enumerate(lines[1:-1]):
    if i[1][1] == '~':
        amnt_of_gas = i[0] * (len(i[1]) - 2)
        break
amnt_of_water = len(lines[1:-1]) * (len(lines[0]) - 2) - amnt_of_gas


new_field = [['.' for _ in range(len(lines))] for _ in range(len(lines[0]))]
new_field[0] = ['#' for _ in range(len(new_field[0]))]
new_field[len(new_field) - 1] = ['#' for _ in range(len(new_field[0]))]
ctr = amnt_of_gas
for i in range(1, len(new_field[1:])):
    new_field[i][0] = '#'
    is_gas = ctr > 0
    for j in range(1, len(new_field[i][1:])):
        new_field[i][j] = '.' if is_gas else '~'
        ctr -= 1
    new_field[i][len(new_field[0])-1] = '#'
for line in new_field:
    print(''.join(line))

padding = 20 + len(f' {max(amnt_of_gas, amnt_of_water)}/{amnt_of_gas+amnt_of_water}')

ratio_str = f' {amnt_of_gas}/{amnt_of_gas+amnt_of_water}'
output_list = ['.'] * round(amnt_of_gas / max(amnt_of_water, amnt_of_gas) * 20)
output_list += [' '] * (padding - len(ratio_str) - len(output_list))
print(''.join(output_list), end='')
print(ratio_str)


ratio_str = f' {amnt_of_water}/{amnt_of_gas+amnt_of_water}'
output_list = ['~'] * round(amnt_of_water / max(amnt_of_water, amnt_of_gas) * 20)
output_list += [' '] * (padding - len(ratio_str) - len(output_list))
print(''.join(output_list), end='')
print(ratio_str)
