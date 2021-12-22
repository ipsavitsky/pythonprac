from fractions import Fraction

inp = eval(input())
S = Fraction(inp[0])
W = Fraction(inp[1])
A_vals = 0
for i in range(inp[2], -1, -1):
    A_vals += Fraction(S ** i) * Fraction(inp[2 + inp[2] - i + 1])
B_vals = 0
for i in range(inp[2 + inp[2] + 2], -1, -1):
    B_vals += Fraction(S ** i) * Fraction(
        inp[2 + inp[2] + 2 + inp[2 + inp[2] + 2] - i + 1]
    )
print(A_vals == W * B_vals if B_vals else False)
