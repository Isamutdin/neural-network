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
        outs = [inputs]

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
            outs = outs[::-1]
            
            e = sum - sample_out
            delta = e*self.df(sum)
            for w in range(1, len(self.weights)):
                self.weights[-w] = self.weights[-w] - lmd*delta*outs[w-1]
                delta = self.weights[-w]*delta*self.df(Array(outs[w-1]))
            
            self.weights[0] = self.weights[0] - delta*lmd*sample_in
                


w1 = Array([Array([random.uniform(-1, 1) for i in range(3)]), Array([random.uniform(-1, 1) for i in range(3)])])
w2 = Array([random.uniform(-1, 1) for i in range(2)])    
w = [w1, w2]
inputs = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
answers = [0.5621765008857981, 0.5499964049315906, 0.5603433768168178, 0.5484841316723525, 0.5615677073606016, 0.5494716026435313, 0.5597248960786497, 0.5477080732029805]

Perceptron = Network_Perceptorn(input_size=3, hiddens=[2], f=sigmoid, df = dsigmoid, weights=w)
Perceptron.train(inputs, answers, 100_000, 0.01)
# for el in inputs:
#     print(Perceptron.go(el))
# print(Perceptron.weights)
