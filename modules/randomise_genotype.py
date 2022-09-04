from random import choice

def randomise_genotype(num_spaces, num_features, num_responses):
    response_options = list(range(num_responses))
    genotype = ""
    for _ in range(num_features ** num_spaces):
        genotype += str(choice(response_options))
    return genotype