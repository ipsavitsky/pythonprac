def Bisect(a, b):
    size = len(b)
    if size == 1:
        if a == b[0]:
            return True
        else:
            return False
    mid = int((size + 1)/2)
    if a == b[mid]:
        return True
    elif a > b[mid]:
        return Bisect(a, b[mid:])
    else:
        return Bisect(a, b[:mid])


sumb, lst = eval(input())
print(Bisect(sumb, lst))
