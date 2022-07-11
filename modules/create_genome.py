def create_genome(spaces, features):
    genome = []
    for x in range(features ** spaces):
        genome.append(x)
    return genome
