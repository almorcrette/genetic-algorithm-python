from random import uniform
from math import floor


def create_genome(spaces, features):
    genome = []
    while len(genome) < features ** spaces:
        position = ''
        for x in range(5):
            position += str(floor(uniform(0, 3)))
        print(position)
        if position not in genome:
            genome.append(position)
        print(genome)
    return genome
