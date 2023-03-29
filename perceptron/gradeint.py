import random
from base import *
from math import exp


w1 = Array([Array([0.3, 0.3, 0]), Array([0.4, -0.5, 1])])
w2 = Array([-0.23, 0.234])
inputs = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
answers = [0.5, 0.5288502407442349, 0.4754071298293779, 0.5060018135126263, 0.5030306057986934, 0.528436950718212, 0.4786834921663368, 0.5081609247363897]


def sigmoid(x):
    return 1/(1 + exp(-x))

def go(w1, w2, el):
    out1 = Array(dot(w1, el))
    sum = [sigmoid(x) for x in out1]
    out2 = dot(w2, sum)
    y = sigmoid(out2)
    return y, out1


def train(W1, W2, inputs, answers):
    lmd = 0.01
    N = 30000
    l_sample = 8
    for n in range(N):
        i = random.randint(0, l_sample-1)
        el = inputs[i]
        an = answers[i]
        y, out = go(W1, W2, el)
        e = y - an
        delta = e*y*(1-y)
        for k in range(len(out)):#корректировка весов на втором слое
            W2[k] = W2[k] - lmd*delta*out[k]

        delta_back = W2*delta*y*(1-y)
        for k in range(len(delta_back)):
            W1[k] = W1[k] - Array(inputs[i])*delta_back[k]*lmd




train(w1, w2, inputs, answers)
print(w1, w2)
# for el in inputs:
#     print(go(w1, w2, el)[0], end=', ')