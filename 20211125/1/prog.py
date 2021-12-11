import sys
st = sys.stdin.buffer.read()
bits = list()
num = st[0]
st = st[1:]
for i in range(num):
    bits.append(st[i*(len(st))//5 : (i+1)*(len(st))//5])

print(''.join(sorted(map(str, bits))))
