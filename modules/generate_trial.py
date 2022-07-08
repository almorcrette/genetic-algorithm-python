from random import uniform
from math import floor
from functools import reduce
import numpy as np

def generate_trial(size, food_proportion):
    __guard_invalid_food_proportion(food_proportion)
    trial = np.zeros((size, size))
    trial = __populate_food(trial, food_proportion)
    return trial

def __guard_invalid_food_proportion(food_proportion):
    if food_proportion > 1 or food_proportion < 0:
        raise Exception('food_proportion must be between 0 and 1') 

def __populate_food(trial, food_proportion):
    size = len(trial)
    for i in range(int(food_proportion * 100)):
        x, y = __select_random_cell(size)
        while trial[y][x] == 1:
            x, y = __select_random_cell(size)
        trial[y][x] = 1
    return trial

def __select_random_cell(size):
    x = __select_random_index(size)
    y = __select_random_index(size)
    return x, y


def __select_random_index(size):
    return floor(uniform(0, size))
    