from functools import partial
from operator import attrgetter
import random
from base import *
from geneticalgorithm.func.func_selection import tournamentSel
from geneticalgorithm.func.func_crossing import crossBlend, crossSimulatedBinary, crossUniform
from geneticalgorithm.func.secondary_functions import *
from geneticalgorithm.base import *
from geneticalgorithm.algorithms import classicGA


BIT_LEN = 3
POPULATION_LEN = 100
CHANCE_CROSSOVER = 1
CHANCE_MUTATION_INDIVID = 0.0
GENERATIONS = 100 #поколения
CHANCE_MUTATION_GEN = 0.2

w1 = Array([[-0.4713077680901974, -0.8613628697696606, -0.47935405618425736], [0.7296388758326728, -0.42449346994609666, -0.6340773148740155]])
w2 = Array([-0.72593973505337, 0.2902096929255349])

def generate_gen():#функция для генерации гена
    return random.uniform(-1, 1)

def sigmoid(x):
    return 1/(1 + exp(-x))

def go(w11):
    inputs = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
    answers = [0.445748164537979, 0.45586021541185057, 0.47480069453322143, 0.4810587587894957, 0.47921909907641547, 0.48742161229055886, 0.503889178190285, 0.5048837487662141]
    mistake = 0
    for i in range(len(inputs)):
        out = dot([[-0.4713077680901974, -0.8613628697696606, -0.47935405618425736], w11], inputs[i])
        sum = [sigmoid(x) for x in out]
        out2 = dot([-0.72593973505337, 0.2902096929255349], sum)
        y = sigmoid(out2)
        mistake += answers[i]-y
    
    
    return abs(mistake)



Fitness.weight = -1 #Указываем будет ли ГА искать максимум или минимум (-1 миниму, а 1 максимум)

creator_gen = partial(generate_gen)

creator_individ = partial(generate_repeat, Individ, BIT_LEN, creator_gen)

creator_population = partial(generate_repeat, list, POPULATION_LEN, creator_individ)

population = creator_population()

for ind in population:
    getattr(ind, 'fitness').setValue(go(ind))

select =  partial(tournamentSel, tournsize=3)
crossover = partial(crossUniform)
mutation = lambda x: x

a = Statistic(lambda x: x)
population, bookeval = classicGA(population, go, select, crossover, mutation, 
   a, CHANCE_CROSSOVER, CHANCE_MUTATION_GEN, GENERATIONS)

print(max(population, key=attrgetter('fitness')), go(max(population, key=attrgetter('fitness'))))

# print(bookeval.get("gen"), bookeval.sections['0'].get('min'))

"""right answer
(3.0; 2.0), (-2.805118; 3.131312), (-3.779310; -3.283186), (3.584458; -1.848126)
"""











# print((np.dot(w1, input)))

# def act(x):
#     return 0 if x < 0.5 else 1

# def go(house, rock, attr):
#     x = np.array([house, rock, attr])
#     w11 = [0.3, 0.3, 0]
#     w12 = [0.4, -0.5, 1]
#     weight1 = np.array([w11, w12])  # матрица 2x3
#     weight2 = np.array([-1, 1])     # вектор 1х2

#     sum_hidden = np.dot(weight1, x)       # вычисляем сумму на входах нейронов скрытого слоя
#     print("Значения сумм на нейронах скрытого слоя: "+str(sum_hidden))

#     out_hidden = np.array([act(x) for x in sum_hidden])
#     print("Значения на выходах нейронов скрытого слоя: "+str(out_hidden))

#     sum_end = np.dot(weight2, out_hidden)
#     y = act(sum_end)
#     print("Выходное значение НС: "+str(y))

#     return y

# house = 1
# rock = 0
# attr = 1

# res = go(house, rock, attr)
# if res == 1:
#     print("Ты мне нравишься")
# else:
#     print("Созвонимся")