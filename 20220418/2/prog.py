class SquareIO:
    def inputCoeff(self, name: str) -> float:
        coef = input(f"Input {name}: ")
        return float(coef)
    
    def printResult(self, result: float):
        print(f"Solution: {result}")


def solveSquare(a, b, c):
    D = b*b - 4 * a * c
    if D > 0:
        x1 = (-b + D**0.5) / (2 * a)
        x2 = (-b - D**0.5) / (2 * a)
        return x1, x2
    elif D == 0:
        x = -b / (2 * a)
        return x, x
    else:
        return None

def main():
    Io = SquareIO()
    a = Io.inputCoeff("a")
    b = Io.inputCoeff("b")
    c = Io.inputCoeff("c")
    result = solveSquare(a, b, c)
    Io.printResult(result)
