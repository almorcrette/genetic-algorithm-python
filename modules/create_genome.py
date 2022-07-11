import itertools


def create_genome(spaces, features):
    genome = []
    digits = ''
    for x in range(features):
        digits += str(x)
    for num in itertools.product(digits, repeat=spaces):
        s = ''.join(num)
        genome.append(s)
    return genome
