import numpy as np
from math import exp


def mul_vectors(a, b) -> int:
    l = len(a)
    assert l == len(b), 'Длинны векторов должны быть равными'
    res = 0
    for i in range(l):
        res += (a[i]*b[i])
    return res

def mul_vector_matrix(a, b) -> list:
    len_matrix = len(b)
    assert len(a) == len_matrix, 'Длина вектора и длина столбцов матрицы должны совпадать'
    res = []
    for i in range(len(b[0])):
        res_mul = 0
        for j in range(len_matrix):
            res_mul += (a[j]*b[j][i])
        res.append(res_mul)
    return res

def mul_matrixs(a, b) -> list:#обычное матричное умножение
    l = len(a)
    assert l==len(b[0]), "Длинна столбцов первой матрицы должно быть равно длинне строк второй матрицы"
    
    res = [[0]*l for _ in range(l)]
    for i in range(l):
        for j in range(l):
            for n in range(l):
                res[i][j] += a[i][n] * b[n][j]
    return res

def mul_matrix_vector(a, b) -> list:#Неккоректно работает
    res = []
    for i in range(len(a)):
        res_mul = 0
        for n in range(len(a[i])):
            res_mul += a[i][n]*b[n%len(b)]
        res.append(res_mul)
    return res

def hyperbolic_tangent(x):
    return (exp(2*x)-1)/(exp(2*x)+1)


def dot(a: list, b: list):
    mul = {
        'TrueTrue': mul_matrixs,
        'TrueFalse': mul_matrix_vector,
        'FalseTrue': mul_vector_matrix,
        'FalseFalse': mul_vectors
    }
    return mul[f'{isinstance(a[0], list)}{isinstance(b[0], list)}'](a, b)