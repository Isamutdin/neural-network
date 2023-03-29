from base import *

def go(w11):
    inputs = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
    answers = [0.0, 1.0, -0.8, 0.2, 0.10000000000000003, 1.0999999999999999, -0.7, 0.30000000000000004]
    
    mistake = 0
    for i in range(len(inputs)):
        sum_hidden = dot([[0.3, 0.3, 0], w11], inputs[i])
        sum_end = dot([-1, 1], sum_hidden)
        mistake += sum_end
    if mistake > 1.2: return 10**6
    return -(mistake)











