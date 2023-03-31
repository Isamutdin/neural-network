import random
from base import *

class Network_Perceptorn:
    def __init__(self, input_size, hiddens, f, df, out_size=1, weights=None) -> None:
        self.input_size = input_size
        self.hiddens = hiddens
        self.f = f
        self.df = df
        self.out_size = out_size
        self.weights = weights

    def go(self, inputs, train=False):
        outs = []

        sum = dot(self.weights[0], inputs)
        for i in range(1, len(self.hiddens)+1):
            out = Array([self.f(x) for x in sum])
            sum = dot(self.weights[i], out)
            outs.append(out)

        if self.out_size==1: return Array([self.f(sum)]), outs
        return Array([self.f(x) for x in sum]), outs

    def train(self, inputs, answers, n, lmd):
        l_sample = len(inputs)
        for _ in range(n):
            k = random.randint(0, l_sample-1)
            sample_in = inputs[k]
            sample_out = answers[k]
            
            sum, outs = self.go(sample_in)
            outs.append(sum)
            for i in range(len(sum)):
                e = sum - sample_out
                delta = e*self.df(sum)
                delta_next = Array([])
                
                for w in range(len(self.weights)):
                    # very hard
                    pass

w1 = Array([[-0.4713077680901974, -0.8613628697696606, -0.47935405618425736], [-0.12964361811150527, -0.8286875079308464, 0.6323587287307706]])
w2 = Array([-0.72593973505337, 0.2902096929255349])    
w = [w1, w2]
inputs = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
answers = [0.5, 0.5288502407442349, 0.4754071298293779, 0.5060018135126263, 0.5030306057986934, 0.528436950718212, 0.4786834921663368, 0.5081609247363897]

Perceptron = Network_Perceptorn(input_size=3, hiddens=[2], f=sigmoid, df = dsigmoid, weights=w)
Perceptron.train(inputs, answers, 1, 0.01)
# (Perceptron.go([0, 0, 0]))
# print(Array([1]) - 1)
