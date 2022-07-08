from random import uniform
from math import floor
from functools import reduce

def generate_trial(food_proportion):
    trial = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    for i in range(int(food_proportion * 100)):
        x = random_0_9()
        print('x: ', x)
        y = random_0_9()
        print('y: ', y)
        while trial[y][x] == 1:
            print('x inside while: ', x)
            x = random_0_9()
            print('y inside while: ', y)
            y = random_0_9()
        trial[y][x] = 1
    
    return trial

def random_0_9():
    return floor(uniform(0, 10))

# trial = generate_trial(0.1)
# print(trial)

# total_food = 0
# for x in trial:
#     total_food += reduce(lambda a, b: a + b, x)
# print(total_food)
