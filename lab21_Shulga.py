﻿# Лабораторная работа № 2.1
# Шульга Е.К., ІО-71
# №  n w    N
# 5(7130)  14 2000 256

import random as r
import math
import matplotlib.pyplot as plt

n = 14
w_max = 2000
N = 256
w_real = [[math.cos(2 * math.pi * i * j / N) for j in range(N)] for i in range(N)]
w_imag = [[math.sin(2 * math.pi * i * j / N) for j in range(N)] for i in range(N)]


def graph():
    x = [0] * N

    for i in range(n):
        A = r.randrange(2)
        W = r.randrange(w_max)
        f = r.randrange(1e9)
        for t in range(N):
            x[t] += A * math.sin(W * t + f)
    return x


def dft(x: list):
    dftt = [[sum(w_real[p][k] * x[k] for k in range(N)), sum(w_imag[p][k] * x[k] for k in range(N))] for p in range(N)]
    return dftt


X = graph()
dftt = dft(X)
data_x = []
data_dft = []
for i in range(len(X)):
    data_x.append(X[i])
    a = math.sqrt(dftt[i][0] ** 2 + dftt[i][1] ** 2)
    data_dft.append(a)
plt.plot([i for i in range(len(data_x))], data_x)
plt.show()
plt.plot([i for i in range(len(data_dft))], data_dft)
plt.show()