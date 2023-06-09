import random
from base import *
from math import exp


# w1 = Array([Array([random.uniform(-1, 1) for i in range(3)]), Array([random.uniform(-1, 1) for i in range(3)])])
# w2 = Array([random.uniform(-1, 1) for i in range(2)])
w1 = Array([[-0.4713077680901974, -0.8613628697696606, -0.47935405618425736], [-0.12964361811150527, -0.8286875079308464, 0.6323587287307706]])
w2 = Array([-0.72593973505337, 0.2902096929255349])
inputs = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
answers = [0.5, 0.5288502407442349, 0.4754071298293779, 0.5060018135126263, 0.5030306057986934, 0.528436950718212, 0.4786834921663368, 0.5081609247363897]


def sigmoid(x):
    return 1/(1 + exp(-x))

def go(w1, w2, el):
    sum1 = (dot(w1, el))
    out1 = Array([sigmoid(x) for x in sum1])
    sum = dot(w2, out1)
    y = sigmoid(sum)
    return y, out1




def train(W1, W2, inputs, answers):
    lmd = 0.0001 #нужно научиться подбирать этот параметр
    N = 1
    l_sample = len(answers )
    for n in range(N):
        i = random.randint(0, l_sample-1)
        el = inputs[i]
        an = answers[i]
        y, out = go(W1, W2, el)
        e = y - an
        delta = e*y*(1-y)
        W2 = W2 - lmd*delta*out

        delta_back = W2*delta*y*(1-y)

        for k in range(len(delta_back)):
            W1[k] = W1[k] - lmd*delta_back[k]*Array(inputs[i])
            print(lmd*delta_back[k]*Array(inputs[i]))



train(w1, w2, inputs, answers)
# print(w1, w2)
# for el in inputs:
#     print(go(w1, w2, el)[0], end=', ')

# print(type(w1[0]))
"""
right answers -> [[0.3, 0.3, 0.0], [0.4, -0.5, 1.0]] [-0.5, 0.5]

при 100_000 -> 
"""