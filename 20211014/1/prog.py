from fractions import Fraction
val = eval(input())
s = Fraction(val[0])
w = Fraction(val[1])
A = 0
for i in range(val[2],-1,-1):
	A += Fraction(s**i) * Fraction(val[2+val[2]-i+1])
B = 0
for i in range(val[2+val[2]+2],-1,-1):
	B += Fraction(s**i) * Fraction(val[2+val[2]+2+val[2+val[2]+2]-i+1])
print(A == w*B)