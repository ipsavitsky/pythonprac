class OrderedComplex(complex):
    def __lt__(self, other):
        return self.real < other.real and self.imag < other.imag


class OrderedComplexMul(OrderedComplex):
    def __matmul__(self, other):
        return self.real * other.real + self.imag * other.imag


A, B = OrderedComplex(1, -5), OrderedComplexMul(10, 15)
print(A < B, B@B)
