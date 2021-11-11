import math
class InvalidInput(Exception):
    pass

class BadTriangle(Exception):
    pass

def TriangleSquare():
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(input())
    except (TypeError, NameError, ValueError) as e:
        raise InvalidInput from e
     
    a = math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))
    b = math.sqrt((x3-x1)**2 + (y3-y1)**2)
    c = math.sqrt((x3-x2)**2 + (y3-y2)**2)
    p = (a+b+c)/2
    area = math.sqrt(p*(p-a)*(p-b)*(p-c))
    if area == 0: # проверить чтобы норм float сравнивался
        raise BadTriangle
    return area


try: 
    res = TriangleSquare()
except BadTriangle:
    print('Not a triangle')
except InvalidInput:
    print('Invalid input')
else:
    print('%.2f' % res)
