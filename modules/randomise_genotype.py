def randomise_genotype(num_spaces, num_features, num_responses):
    genotype = ""
    for _ in range(num_features ** num_spaces):
        genotype += "6"
    return genotype