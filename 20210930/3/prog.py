f_list = eval(input())
matr1 = [f_list]
for i in range(len(f_list) - 1):
    matr1.append(eval(input()))

matr2 = []
for i in range(len(f_list)):
    matr2.append(eval(input()))

res = [[j for j in range(len(matr2))] for i in range(len(matr1))]
for i in range(len(matr1)):
    for j in range(len(matr2)):
        s = 0
        for k in range(len(matr1)):
            s += matr1[i][k] * matr2[k][j]
        res[i][j] = s

for i in res:
    print(i)
