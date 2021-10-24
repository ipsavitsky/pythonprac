st = input().lower()
pairs = set()
for i in range(len(st)-1):
    if str.isalpha(st[i:i+2]):
        pairs.add(st[i:i+2])
print(len(pairs))