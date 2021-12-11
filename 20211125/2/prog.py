import sys

data = sys.stdin.buffer.read()
print(data.decode().encode('latin1', errors='replace').decode('cp1251', errors='replace'))