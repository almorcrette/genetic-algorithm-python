def create_genome(spaces, features):
    genome = []
    genome.extend(range(features ** spaces))
    return genome
