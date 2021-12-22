import sys

st = sys.stdin.buffer.read()
bits = list()
num = st[0]
nw = st[0:1]
st = st[1:]
for i in range(num):
    bits.append(st[i * (len(st)) // num : (i + 1) * (len(st)) // num])

print((nw + b''.join(sorted(bits))).decode())
