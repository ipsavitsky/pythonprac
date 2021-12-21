import sys

data = sys.stdin.buffer.read().decode().strip()
print(data.encode('latin1', errors='replace').decode('cp1251', errors='replace'))