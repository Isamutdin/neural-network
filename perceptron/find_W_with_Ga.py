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

def generate_gen():#функция для генерации гена
    return random.uniform(-1, 1)


def go(w11):
    inputs = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
    answers = [0.0, 1.0, -0.8, 0.2, 0.10000000000000003, 1.0999999999999999, -0.7, 0.30000000000000004]
    
    mistake = 0
    for i in range(len(inputs)):
        sum_hidden = dot([[0.3, 0.3, 0], w11], inputs[i])
        sum_end = dot([-1, 1], sum_hidden)
        mistake += answers[i]-sum_end
    
    if -mistake > 0: return -10**6
    return -(mistake)



Fitness.weight = 1 #Указываем будет ли ГА искать максимум или минимум (-1 миниму, а 1 максимум)

creator_gen = partial(generate_gen)

creator_individ = partial(generate_repeat, Individ, BIT_LEN, creator_gen)

creator_population = partial(generate_repeat, list, POPULATION_LEN, creator_individ)

population = creator_population()

for ind in population:
    getattr(ind, 'fitness').setValue(go(ind))

select =  partial(tournamentSel, tournsize=3)
crossover = partial(crossBlend, alpha=0.5)
mutation = lambda x: x

a = Statistic(lambda x: x)
population, bookeval = classicGA(population, go, select, crossover, mutation, 
   a, CHANCE_CROSSOVER, CHANCE_MUTATION_GEN, GENERATIONS)

print(max(population, key=attrgetter('fitness')), go(max(population, key=attrgetter('fitness'))))

# print(bookeval.get("gen"), bookeval.sections['0'].get('min'))

"""right answer
(3.0; 2.0), (-2.805118; 3.131312), (-3.779310; -3.283186), (3.584458; -1.848126)
"""
# print(int(2.5368596112684827e-14))





def go():
    w11 = [0.3, 0.3, 0]
    w12 = [0.4, -0.5, 1]
    inputs = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
    answers = [0.0, 1.0, -0.8, 0.2, 0.10000000000000003, 1.0999999999999999, -0.7, 0.30000000000000004,]
    
    mistake = 0
    for i in range(len(inputs)):
        sum_hidden = dot([w11, w12], inputs[i])
        sum_end = dot([-1, 1], sum_hidden)
        mistake += sum_end
        print(sum_end, end=', ')
    print()
    return mistake




print(go())






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