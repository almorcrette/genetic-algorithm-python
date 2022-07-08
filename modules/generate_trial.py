from random import uniform
from math import floor
from functools import reduce
import numpy as np

def generate_trial(size, food_proportion):
    if food_proportion > 1 or food_proportion < 0:
        raise Exception('food_proportion must be between 0 and 1') 
    trial = np.zeros((size, size))
    for i in range(int(food_proportion * 100)):
        x = random_0_9()
        y = random_0_9()
        while trial[y][x] == 1:
            x = random_0_9()
            y = random_0_9()
        trial[y][x] = 1
    
    return trial

def random_0_9():
    return floor(uniform(0, 10))
